import sqlite3

conn = sqlite3.connect('news.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM news ORDER BY date')
rows = cursor.fetchall()

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Table</title>
</head>
<body>
    <h1 style="center">News Table</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Date</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
"""

for row in rows:
    html_content += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td><a href="{row[3]}" target="_blank">whoever doesn't click is gay</a></td>
            </tr>
    """

html_content += """
        </tbody>
    </table>
</body>
</html>
"""

with open("output.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("The HTML file has been generated or updated: output.html")

conn.close()