import shelve

if __name__ == "__main__":
    db = shelve.open('storage.db', 'r')
    pt_visits = db['ptVisits']

    print(pt_visits['T1111111E'].get_drug_list().split(','))
