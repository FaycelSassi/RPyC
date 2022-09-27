import rpyc
import GestionEntree

class MyService(rpyc.Service):
    global Element
    Element={}
    def on_connect(self, conn):
        from datetime import datetime 
        now = datetime.now() # datetime object containing current date and time
        dtstring = now.strftime("%d/%m/%Y %H:%M:%S")# dd/mm/YY H:M:S
        print("un utilisateur a connecté à", dtstring)         
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        from datetime import datetime
        now = datetime.now()  # datetime object containing current date and time 
        dtstring = now.strftime("%d/%m/%Y %H:%M:%S")# dd/mm/YY H:M:S
        print("un utilisateur a quitté à", dtstring)
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    
    def exposed_init(self): # this is an exposed method
        return GestionEntree.init()
    
    def exposed_afftous(self): # this is an exposed method
        return GestionEntree.afftous(Element)
        
    
    def exposed_ajouterEntree(self,a,b): # this is an exposed method
        global Element
        return GestionEntree.ajouterEntree(a,b,Element)
         
    def exposed_trouverNumero(self,nom): # this is an exposed method
        global Element
        return GestionEntree.trouverNumero(nom,Element)

    def exposed_nbNumeros(self): # this is an exposed method
        global Element
        return GestionEntree.nbNumeros(Element)
    

    def exposed_supprimerEntree(self,nom): # this is an exposed method
        global Element
        return GestionEntree.supprimerEntree(nom,Element)
    
    def exposed_supprimerTout(self): # this is an exposed method
        global Element
        return GestionEntree.supprimerTout(Element)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
