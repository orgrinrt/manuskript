# -*- coding: utf-8 -*-

import pickle
import pprint
from enums import *
from qt import *
import collections

viewSettings = {
    "Tree": {
        "Icon": "Nothing",
        "Text": "Compile",
        "Background": "Nothing",
        "InfoFolder": "Nothing",
        "InfoText": "Nothing",
        },
    "Cork": {
        "Icon": "Nothing",
        "Text": "Nothing",
        "Background": "Nothing",
        "Corner": "Label",
        "Border": "Nothing",
        },
    "Outline": {
        "Icon": "Nothing",
        "Text": "Compile",
        "Background": "Nothing",
        },
    }
    
spellcheck = False
dict = None
corkSizeFactor = 100
folderView = "cork"
lastTab = 0
openIndexes = [""]
autoSave = False
autoSaveDelay = 5
autoSaveNoChanges = True
autoSaveNoChangesDelay = 5
saveOnQuit = True
outlineViewColumns = [Outline.title.value, Outline.POV.value, Outline.status.value, 
                      Outline.compile.value, Outline.wordCount.value, Outline.goal.value, 
                      Outline.goalPercentage.value, Outline.label.value]
corkBackground = {
    "color": "#926239",
    "image": ""
        }
defaultTextType = "t2t"
fullScreenTheme = "spacedreams"

textEditor = {
    "background": "fff",
    "fontColor": "#000",
    "font": qApp.font().toString(),
    "misspelled": "#F00",
    "lineSpacing": 100,
    "tabWidth": 20,
    "indent": True,
    "spacingAbove": 5,
    "spacingBelow": 5,
    }
    
revisions = {
    "keep": True,
    "smartremove": True,
    "rules": collections.OrderedDict({
        10 * 60:            60,                     # One per minute for the last 10mn
        60 * 60:            60 * 10,                # One per 10mn for the last hour
        60 * 60 * 24:       60 * 60,                # One per hour for the last day
        60 * 60 * 24 * 30:  60 * 60 * 24,           # One per day for the last month
        None:               60 * 60 * 24 * 7,       # One per week for eternity
        })
    }
    
def save(filename=None):
    
    global spellcheck, dict, corkSliderFactor, viewSettings, corkSizeFactor, folderView, lastTab, openIndexes, \
           autoSave, autoSaveDelay, saveOnQuit, autoSaveNoChanges, autoSaveNoChangesDelay, outlineViewColumns, \
           corkBackground, fullScreenTheme, defaultTextType, textEditor, revisions
    
    allSettings = {
        "viewSettings": viewSettings,
        "dict": dict,
        "spellcheck": spellcheck,
        "corkSizeFactor": corkSizeFactor,
        "folderView": folderView,
        "lastTab": lastTab,
        "openIndexes": openIndexes,
        "autoSave":autoSave,
        "autoSaveDelay":autoSaveDelay,
        "saveOnQuit":saveOnQuit,
        "autoSaveNoChanges":autoSaveNoChanges,
        "autoSaveNoChangesDelay":autoSaveNoChangesDelay,
        "outlineViewColumns":outlineViewColumns,
        "corkBackground":corkBackground,
        "fullScreenTheme":fullScreenTheme,
        "defaultTextType":defaultTextType,
        "textEditor":textEditor,
        "revisions":revisions,
        }
    
    #pp=pprint.PrettyPrinter(indent=4, compact=False)
    #print("Saving:")
    #pp.pprint(allSettings)
    
    if filename:
        f = open(filename, "wb")
        pickle.dump(allSettings, f)
    else:
        return pickle.dumps(allSettings)
    
def load(string, fromString=False):
    """Load settings from 'string'. 'string' is the filename of the pickle dump.
    If fromString=True, string is the data of the pickle dumps."""
    global allSettings
    
    if not fromString:
        try:
            f = open(string, "rb")
            allSettings = pickle.load(f)
            
        except:
            print("{} doesn't exist, cannot load settings.".format(string))
            return
    else:
        allSettings = pickle.loads(string)
    
    #pp=pprint.PrettyPrinter(indent=4, compact=False)
    #print("Loading:")
    #pp.pprint(allSettings)
    
    if "viewSettings" in allSettings:
        global viewSettings
        viewSettings = allSettings["viewSettings"]
        
    if "dict" in allSettings:
        global dict
        dict = allSettings["dict"]
        
    if "spellcheck" in allSettings:
        global spellcheck
        spellcheck = allSettings["spellcheck"]
        
    if "corkSizeFactor" in allSettings:
        global corkSizeFactor
        corkSizeFactor = allSettings["corkSizeFactor"]
        
    if "folderView" in allSettings:
        global folderView
        folderView = allSettings["folderView"]
        
    if "lastTab" in allSettings:
        global lastTab
        lastTab = allSettings["lastTab"]
        
    if "openIndexes" in allSettings:
        global openIndexes
        openIndexes = allSettings["openIndexes"]
        
    if "autoSave" in allSettings:
        global autoSave
        autoSave = allSettings["autoSave"]
        
    if "autoSaveDelay" in allSettings:
        global autoSaveDelay
        autoSaveDelay = allSettings["autoSaveDelay"]
        
    if "saveOnQuit" in allSettings:
        global saveOnQuit
        saveOnQuit = allSettings["saveOnQuit"]
        
    if "autoSaveNoChanges" in allSettings:
        global autoSaveNoChanges
        autoSaveNoChanges = allSettings["autoSaveNoChanges"]
        
    if "autoSaveNoChangesDelay" in allSettings:
        global autoSaveNoChangesDelay
        autoSaveNoChangesDelay = allSettings["autoSaveNoChangesDelay"]
        
    if "outlineViewColumns" in allSettings:
        global outlineViewColumns
        outlineViewColumns = allSettings["outlineViewColumns"]
    
    if "corkBackground" in allSettings:
        global corkBackground
        corkBackground = allSettings["corkBackground"]
        
    if "fullScreenTheme" in allSettings:
        global fullScreenTheme
        fullScreenTheme = allSettings["fullScreenTheme"]
        
    if "defaultTextType" in allSettings:
        global defaultTextType
        defaultTextType = allSettings["defaultTextType"]

    if "textEditor" in allSettings:
        global textEditor
        textEditor = allSettings["textEditor"]

    if "revisions" in allSettings:
        global revisions
        revisions = allSettings["revisions"]