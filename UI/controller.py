import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """

        try :
            valore = int(self._view.guadagno_medio_minimo.value)

            # chiamare la costruzione del grafo
            self._model.costruisci_grafo(valore)
            graph = self._model.G
            self._view.lista_visualizzazione.controls.clear()

            self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di Hubs: {self._model.get_num_nodes()}'))
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f'Numero di Tratte: {self._model.get_num_edges()}'))

            idx = 1
            for hubO in graph:
                for hubD in graph[hubO]:
                    text = f'{idx}) [{hubO} -> {hubD}] -- guadagno Medio Per Spedizione: {graph[hubO][hubD]['weight']}'
                    self._view.lista_visualizzazione.controls.append(ft.Text(text))
                    idx += 1

            self._view.update()
        except ValueError:
            self._view.show_alert('Inserire un valore adatto!')