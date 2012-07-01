#!/usr/bin/env python

import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)
    
    
from config import ProxyConfig

config = ProxyConfig()

class Win:

    def __init__(self):

        #Set the Glade file
        self.gladefile = "config.glade"  
        self.wTree = gtk.glade.XML(self.gladefile, "mainWindow") 

        #Create our dictionay and connect it
        dic = {"on_mainWindow_destroy" : gtk.main_quit
               , "on_Add" : self.OnAdd
               , "on_rm" : self.OnRm
               , "on_save" : self.OnSave
               , "on_des" : self.on_destroy
               }
        
        self.wTree.signal_autoconnect(dic)

        #Prior
        self.cUser = 0
        self.cPassw = 1
        
        #name
        self.sUser = "Nom"
        self.sPassw = "Mot de passe"

        #Get the treeView from the widget Tree
        self.View = self.wTree.get_widget("View")
        
        #Add all of the List Columns to the View
        self.AddListColumn(self.sUser, self.cUser)
        #self.AddListColumn(self.sPassw, self.cPassw)

        #Create the listStore Model to use with the View
        self.accList = gtk.ListStore(str, str)
        
        #Attache the model to the treeView
        self.View.set_model(self.accList)
        
        
        self.status = self.wTree.get_widget('statusbar1')
        
        
        self.__load()

    def AddListColumn(self, title, columnId):
        """This function adds a column to the list view.
        First it create the gtk.TreeViewColumn and then set
        some needed properties"""

        column = gtk.TreeViewColumn(title, gtk.CellRendererText()
                                    , text=columnId)
        column.set_resizable(True)		
        column.set_sort_column_id(columnId)
        self.View.append_column(column)
    
    #----------------------------------------------------------------------
    def OnAdd(self, widget):
        
        """Called when the user wants to add """
        
        self.status.remove_all(0)
        
        #Cteate the dialog, show it, and store the results
        addAccDlg = addDialog();
        result, newAcc = addAccDlg.run()

        if (result == gtk.RESPONSE_OK and newAcc.user is not ''):
            """The user clicked Ok"""
            self.accList.append(newAcc.getList())
        #print self.getAll()[0]
        
         
    def OnRm(self, widget):
        """Remove current Selected Row"""
        
        self.status.remove_all(0)
        
        entry1, path = self.View.get_selection().get_selected()
        #print entry1[path][0],entry1[path][1]
        try:
            self.accList.remove(path)
        except:
            pass
    
    def OnSave(self, widget):
        """"""
        try:
            config.deleteAll()
            for accinfo in self.getAll():
                #print accinfo
                config.setLogin(**accinfo.toDict())
            #print 'ok'
            self.status.push(0,'Sauvegarde ok.')
        except:
            self.status.push(0,'Erreur !')
        
        
    #----------------------------------------------------------------------
    def getAll(self):
        """"""
        return tuple(AccNfo(row[0], row[1]) for row in self.accList )
    
    
    #----------------------------------------------------------------------
    def __load(self):
        """Load account info stored in DB"""
        allacc = config.getAllacc()
        allacc = tuple(AccNfo(**acc) for acc in allacc)
        for acc in allacc: # TODO map() ?
            self.accList.append(acc.getList())
            
        self.status.push(0,'Chargement ok.')
            
    
    def on_destroy(self,widget):
        
        gtk.main_quit()
        
        
        

class addDialog:
    """This class is used to show Dialog"""

    def __init__(self, user="", passw=""):

        #setup the glade file
        self.gladefile = "config.glade"
        
        self.accinfo = AccNfo(user, passw)

    def run(self):
        """This function will show the Add Dialog"""	

        #load the dialog from the glade file	  
        self.wTree = gtk.glade.XML(self.gladefile, "addDlg") 
        #Get the actual dialog widget
        self.dlg = self.wTree.get_widget("addDlg")

        #run the dialog and store the response		
        self.result = self.dlg.run()
        #get the value of the entry fields
        self.accinfo.user = self.wTree.get_widget("in_acc").get_text()
        self.accinfo.passw = self.wTree.get_widget("in_passw").get_text()

        #we are done with the dialog, destory it
        self.dlg.destroy()

        #return the result and the accinfo 
        return self.result, self.accinfo


        
    
class AccNfo:
    """This class represents all the informations"""

    def __init__(self, user="", passw=""):

        self.user = user
        self.passw = passw

    def getList(self):
        """This function returns a list made up of the Class member"""
        return [self.user, self.passw]
    
    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return str(self.getList())
    
    def toDict(self):
        return {'user':self.user,'passw':self.passw}
        
    
    

if __name__ == "__main__":
    print 0
    w = Win()
    print 1
    gtk.main()
    print 2
