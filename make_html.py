import pandas as pd
from utils import helper as hp
import schedule
from datetime import datetime
import time 
import sys
from utils.config_util import Config
c = Config('configs/url_config.yaml')
URLS = c.config['URLS']
previos_hash = None
def run_all():
    global previos_hash
    time_now = datetime.now().strftime("%H:%M:%S") 
    print('running the script at ' , time_now)
    
    medals_json = hp.fetch_json(URLS['MEDALS_URL'])
    hash_this = hp.hash_json(medals_json)
    if previos_hash and previos_hash == hash_this:
        
        print('No new data')
        return 
    previos_hash = hash_this
    hp.save_json(medals_json, f'jsons/medals_{time_now}.json')

    medal_tables = medals_json['medalStandings']['medalsTable']
    total_medals = [] 
    _rank = []
    for each in medal_tables:
        organisation = each['organisation']
        medals_number_list = each['medalsNumber']
        _rank.append(each['rank'])
        total_obj = [t for t in medals_number_list if t['type'] == 'Total'][0]
        # del total_obj['type']
        total_obj['organisation'] = organisation
        total_obj['rank'] = each['rank']
        total_medals.append(total_obj)
        
    noc_df = pd.read_csv('csvs/noc.csv')    
    medals_df = pd.DataFrame(total_medals)
    medals_df['country'] = medals_df['organisation'].apply(lambda x: noc_df[noc_df['noc_code'] == x]['noc_name'].values[0])
    medals_df.drop(columns=['type'], inplace=True)
    medals_df.to_csv(f'csvs/medals_{time_now}.csv', index=False)


    # Assuming df is your dataframe
    df = medals_df.copy()

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Medal Table</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 20px;
                display: flex;
                justify-content: center;
                align-items: flex-start; /* Changed from center to flex-start */
                height: 100vh;
            }
            .table-container {
                width: 80%;
                max-width: 800px;
                margin: 0 auto;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                font-size: 1em;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }
            thead {
                background-color: #007bff;
                color: #ffffff;
                text-align: left;
            }
            th, td {
                padding: 12px 15px;
            }
            tbody tr {
                border-bottom: 1px solid #dddddd;
            }
            tbody tr:nth-of-type(even) {
                background-color: #f3f3f3;
            }
            tbody tr:last-of-type {
                border-bottom: 2px solid #007bff;
            }
            tbody tr.active-row {
                font-weight: bold;
                color: #007bff;
            }
        </style>
        <!-- DataTables CSS -->
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">
        <!-- jQuery -->
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <!-- DataTables JS -->
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <div class="table-container">
            <h1>Medal Table last updated at """ + time_now + """</h1>
            <table id="medalTable" class="display">
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Gold</th>
                        <th>Silver</th>
                        <th>Bronze</th>
                        <th>Total</th>
                        <th>Country</th>
                        
                    </tr>
                </thead>
                <tbody>
    """

    for index, row in df.iterrows():
        html += f"""
                    <tr>
                        <td>{row['rank']}</td>
                        <td>{row['gold']}</td>
                        <td>{row['silver']}</td>
                        <td>{row['bronze']}</td>
                        <td>{row['total']}</td>
                        <td>{row['country']}</td>
                    </tr>
        """

    html += """
                </tbody>
            </table>
        </div>
         <script>
    $(document).ready(function() {
        $('#medalTable').DataTable();
    });
</script>
    </body>
    </html>
    """

    # Save the HTML to a file
    with open("medal_table.html", "w") as file:
        file.write(html)


# schedule.every(30).minutes.do(run_all)
schedule.every(10).minutes.do(run_all)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        #  if argument provided, run the script once
        run_all()
    else:
    
        while True:
            schedule.run_pending()
            time.sleep(1)