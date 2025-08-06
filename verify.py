import pandas as pd

atp = pd.read_csv("atp_singles.csv")
wta = pd.read_csv("wta_singles.csv")

def standardize_tourney_names(df, replacements):
    for original, new in replacements.items():
        df.loc[df["tourney_name"] == original, "tourney_name"] = new
    return df


def fix_wta_names(wta):
    replacements = {
        "Us Open": "US Open",
        "Rome": "Rome Masters",
        "Cincinnati": "Cincinnati Masters",
        "Madrid": "Madrid Masters",
        "Miami": "Miami Masters",
        "Indian Wells": "Indian Wells Masters",
        "S-Hertogenbosch": "s Hertogenbosch",
        "s-Hertogenbosch": "s Hertogenbosch",
        "'s Hertogenbosch": "s Hertogenbosch",
    }
    return standardize_tourney_names(wta, replacements)


def fix_atp_names(atp):
    replacements = {
        "Us Open": "US Open",
        "Rio Olympics": "Olympics",
    }
    return standardize_tourney_names(atp, replacements)


def resolve_tourney_id_conflicts(atp, wta):
    atp_ids = atp[["tourney_id", "tourney_name"]].drop_duplicates()
    wta_ids = wta[["tourney_id", "tourney_name"]].drop_duplicates()

    merged = pd.merge(atp_ids, wta_ids, on="tourney_id", how="inner", suffixes=("_ATP", "_WTA"))
    mismatches = merged[merged["tourney_name_ATP"] != merged["tourney_name_WTA"]]

    print("Conflicting tourney_id entries:", mismatches.shape[0])
    print(mismatches.head(10))

    ids_to_fix = mismatches["tourney_id"].unique()

    atp["tourney_id"] = atp.apply(
        lambda row: row["tourney_id"] + "_m" if row["tourney_id"] in ids_to_fix else row["tourney_id"], axis=1
    )
    wta["tourney_id"] = wta.apply(
        lambda row: row["tourney_id"] + "_f" if row["tourney_id"] in ids_to_fix else row["tourney_id"], axis=1
    )

    return atp, wta

atp = fix_atp_names(atp)
wta = fix_wta_names(wta)
atp, wta = resolve_tourney_id_conflicts(atp, wta)

# Zapisanie oczyszczonych danych
atp.to_csv("atp_singles.csv", index=False)
wta.to_csv("wta_singles.csv", index=False)

