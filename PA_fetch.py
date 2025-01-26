import pandas as pd

# Creating the DataFrame with the rounded data
data = {
    "County": [
        "Adams", "Allegheny", "Armstrong", "Beaver", "Bedford", "Berks", "Blair", "Bradford", "Bucks", "Butler", 
        "Cambria", "Cameron", "Carbon", "Centre", "Chester", "Clarion", "Clearfield", "Clinton", "Columbia", "Crawford", 
        "Cumberland", "Dauphin", "Delaware", "Elk", "Erie", "Fayette", "Forest", "Franklin", "Fulton", "Greene", "Huntingdon", 
        "Indiana", "Jefferson", "Juniata", "Lackawanna", "Lancaster", "Lawrence", "Lebanon", "Lehigh", "Luzerne", "Lycoming", 
        "McKean", "Mercer", "Mifflin", "Monroe", "Montgomery", "Northampton", "Northumberland", "Perry", "Philadelphia", "Pike", 
        "Potter", "Schuylkill", "Snyder"
    ],
    "Average Death Rate (2015-2018)": [
        17, 46, 50, 39, 21, 22, 28, 26, 29, 34, 56, 0, 38, 10, 21, 20, 15, 17, 24, 31, 22, 34, 38, 18, 32, 42, 11, 21, 
        29, 37, 18, 42, 16, 10, 41, 22, 46, 17, 39, 47, 25, 19, 31, 21, 30, 24, 24, 26, 21, 62, 20, 11, 34, 8
    ],
    "Estimated Number of People Represented": [
        18, 562, 34, 66, 10, 95, 34, 16, 187, 64, 77, 0, 25, 11, 115, 7, 12, 7, 16, 27, 58, 94, 219, 6, 90, 55, 11, 33, 
        4, 13, 8, 37, 7, 2, 88, 121, 42, 15, 146, 150, 29, 8, 36, 10, 51, 208, 75, 24, 10, 961, 11, 2, 50, 3
    ]
}

df = pd.DataFrame(data)

# Exporting the DataFrame to a CSV file
file_path = '/Users/arsh/Documents/vscode/DrugOverdose/overdose_deaths_by_county.csv'
df.to_csv(file_path, index=False)

file_path
