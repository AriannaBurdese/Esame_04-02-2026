from database.DB_connect import DBConnect
from model.artist import Artist


class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT role
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            ruolo = (row)
            result.append(ruolo)

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_nodi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = (""" select artist_id, name
                    from artists a, authorship au
                    where a.artist_id = au.artist_id and au.role = %s """)
        try:
            cursor.execute(query)
            for row in cursor:
                artist = Artist(artist_id=row['artist_id'], name=row['name'])
                result.append(artist)


        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_connessioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = ("""select a1.artist_id as id1, a2.artist_id as id2, COUNT(DISTINCT o1.object_id) as indice
                    from artists a1, artists a2, authorship au1, authorship au2, objects o1, objects o2
                    where a1.artist_id = au1.artist_id 
		                and a2.artist_id = au2.artist_id and au1.object_id =o1.object_id and au2.object_id =o2.object_id
		                and a1.artist_id < a2.artist_id and o1.curator_approved = 1 and o2.curator_approved = 1 and au1.role = "Designer" and  au2.role = "Designer"
                    group by id1, id2
		 """)
        try:
            cursor.execute(query)
            for row in cursor:
                connessione = (row["id1"], row["id2"], row["indice"])
                result.append(connessione)


        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result



