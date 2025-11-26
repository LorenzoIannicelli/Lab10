from database.DB_connect import DBConnect
from model.hub import Hub
from model.arco import Arco

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def read_all_hub():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print('Connessione fallita.')
            return None
        else :
            cursor = cnx.cursor(dictionary=True)
            query = ("SELECT * "
                     "FROM hub h")
            cursor.execute(query)

            for row in cursor :
                hub = Hub(row['id'],
                          row['codice'],
                          row['nome'],
                          row['citta'],
                          row['stato'],
                          row['latitudine'],
                          row['longitudine'])

                result.append(hub)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def read_all_spedizioni(threshold):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print('Connessione fallita.')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT LEAST(id_hub_origine, id_hub_destinazione) AS origine,
                               GREATEST(id_hub_origine, id_hub_destinazione) as destinazione,
                               AVG(valore_merce) as avg_valore_merce
                        FROM spedizione
                        GROUP BY origine, destinazione
                        HAVING avg_valore_merce >= %s"""
            cursor.execute(query, (threshold,))

            for row in cursor:
                arco = Arco(row['origine'],
                          row['destinazione'],
                          row['avg_valore_merce'])

                result.append(arco)

        cursor.close()
        cnx.close()
        return result