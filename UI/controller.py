import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model



    """def populate_dd(self):
        self._view.dd_ruolo.clean()
        if self._model._role_list is not None:
            for ruolo in self._model._role_list:
                self._view.dd_ruolo.options.append(ft.dropdown.Option(text = ruolo))
        else:
            return None
        self._view._page.update()"""


    def handle_crea_grafo(self, e, ruoli):
        try:
            ruolo = (self._view.dd_ruolo.value)
        except:
            self._view.show_alert("Selezionare un ruolo")
        ruoli = self._model._role_list
        self._view.popola_dropdown_ruolo(ruoli)
        self._view._page.update()

    def handle_classifica(self, e):
        pass