import matplotlib.pyplot as plt
import numpy as np

teams = {
    "קטר": "Qatar",
    "אקוודור": "Ecuador",
    "סנגל": "Senegal",
    "הולנד": "The Netherlands",
    "אנגליה": "England",
    "איראן": "Iran",
    "ארצות הברית": "USA",
    "ווילס": "Wales",
    "ארגנטינה": "Argentina",
    "ערב הסעודית": "Saudi Arabia",
    "מקסיקו": "Mexico",
    "פולין": "Poland",
    "צרפת": "France",
    "אוסטרליה": "Australia",
    "דנמרק": "Denmark",
    "תוניסיה": "Tunisia",
    "ספרד": "Spain",
    "קוסטה ריקו": "Costa Rica",
    "גרמניה": "Germany",
    "יפן": "Japan",
    "בלגיה": "Belgium",
    "קנדה": "Canada",
    "מרוקו": "Morocco",
    "קרואטיה": "Croatia",
    "ברזיל": "Brazil",
    "סרביה": "Serbia",
    "שוויץ": "Switzerland",
    "קמרון": "Cameroon",
    "פורטוגל": "Portugal",
    "גאנה": "Ghana",
    "אורוגוואי": "Uruguay",
    "קוריאה הדרומית": "Korea Republic",
    "Qatar": "קטר",
    "Ecuador": "אקוודור",
    "Senegal": "סנגל",
    "The Netherlands": "הולנד",
    "England": "אנגליה",
    "Iran": "איראן",
    "USA": "ארצות הברית",
    "Wales": "ווילס",
    "Argentina": "ארגנטינה",
    "Saudi Arabia": "ערב הסעודית",
    "Mexico": "מקסיקו",
    "Poland": "פולין",
    "France": "צרפת",
    "Australia": "אוסטרליה",
    "Denmark": "דנמרק",
    "Tunisia": "תוניסיה",
    "Spain": "ספרד",
    "Costa Rica": "קוסטה ריקו",
    "Germany": "גרמניה",
    "Japan": "יפן",
    "Belgium": "בלגיה",
    "Canada": "קנדה",
    "Morocco": "מרוקו",
    "Croatia": "קרואטיה",
    "Brazil": "ברזיל",
    "Serbia": "סרביה",
    "Switzerland": "שוויץ",
    "Cameroon": "קמרון",
    "Portugal": "פורטוגל",
    "Ghana": "גאנה",
    "Uruguay": "אורוגוואי",
    "Korea Republic": "קוריאה הדרומית",
}

if __name__ == '__main__':
    data = np.genfromtxt("world_cup_res.csv", delimiter=",", skip_header=1, dtype=str)

    unique, counts = np.unique(data[:, 2], return_counts=True)
    unique = [teams[t] for t in unique]  # replace names to English (list comprehension python)
    # n_unique = []
    # for t in unique:
    #     n_unique.append(teams[t])
    # unique = n_unique

    results = np.vstack((unique, counts)).transpose()

    counts_column = results[:, 1].astype(np.int32)
    top_res = results[counts_column > counts_column.mean()]

    plt.bar(top_res[:, 0], top_res[:, 1].astype(np.int32), color=['red', '#81acff', 'yellow', 'blue'])
    plt.show()

    winner_team = results[counts_column == counts_column.max()][0, 0]
    print(data[data[:, 2] == teams[winner_team]][:, 1])
