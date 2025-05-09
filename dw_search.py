enemies = {
    "autons": ["Rose (2005)", "The Pandorica Opens (2010)"],
    "nestene consciousness": ["Rose (2005)"],
    "lady cassandra": ["The End of the World (2005)"],
    "the gelth": ["The Unquiet Dead (2005)"],
    "slitheen": ["Aliens of London (2005)", "World War Three (2005)", "Boom Town (2005)"],
    "dalek": ["Dalek (2005)", "Bad Wolf (2005)", "The Parting of The Ways (2005)", "Army of Ghosts (2006)", "Doomsday (2006)", "The Stolen Earth (2008)", "Journey's End (2008)", "Victory of The Daleks (2010)", "The Pandorica Opens (2010)"],
    "the editor": ["The Long Game (2005)"],
    "the mighty jagrafess of the holy hadrojassic maxarodenfoe": ["The Long Game (2005)"],
    "reapers": ["Father's Day (2005)"],
    "the empty child": ["The Empty Child (2005)", "The Doctor Dances (2005)"],
    "cybermen": ["The Rise of the Cybermen (2006)", "The Age of Steel (2006)", "Army of Ghosts (2006)", "The Pandorica Opens (2010)"],
    "the wire": ["The Idiot's Lantern (2006)"],
    "clockwork droids": ["The Girl in The Fireplace (2006)"],
    "krillitane": ["School Reunion (2006)"],
    "the beast": ["The Impossible Planet (2006)", "The Satan Pit (2006)"],
    "ood": ["The Impossible Planet (2006)", "The Satan Pit (2006)", "Planet of The Dead (2008)"],
    "cult of skaro": ["Army of Ghosts (2006)", "Doomsday (2006)"],
    "plasmavore": ["Smith and Jones (2007)"],
    "judoon": ["Smith and Jones (2007)", "The Pandorica Opens (2010)"],
    "the master": ["Utopia (2007)", "The Sound of Drums (2007)", "The Last of The Time Lords (2007)"],
    "weeping angels": ["Blink (2007)", "The Time of Angels (2010)", "Flesh and Stone (2010)"],
    "professor lazarus": ["The Lazarus Experiment (2007)"],
    "family of blood": ["Human Nature (2007)", "The Family of Blood (2007)"],
    "carrionites": ["The Shakespeare Code (2007)"],
    "macra": ["Gridlock (2007)"],
    "futurekind": ["Utopia (2007)"],
    "toclafane": ["The Sound of Drums (2007)", "Last of The Time Lords (2007)"],
    "adipose": ["Partners in Crime (2008)"],
    "miss foster": ["Partners in Crime (2008)"],
    "pyrovile": ["The Fires of Pompeii (2008)"],
    "sontarans": ["The Sontaran Stratagem (2008)", "The Poison Sky (2008)", "The Pandorica Opens (2010)"],
    "Lucius Dextrus": ["The Fires of Pompeii (2008)"],
    "The Vespiform": ["The Unicorn and The Wasp (2008)"],
    "the midnight entity": ["Midnight (2008)"],
    "davros": ["The Stolen Earth (2008)", "Journey's End (2008)"],
    "time beetle": ["Turn Left (2008)"],
    "vashta nerada": ["Silence in The Library (2008)", "Forest of The Dead (2008)"],
    "the shadow proclamation": ["The Stolen Earth (2008)"],
    "prisoner zero": ["The Eleventh Hour (2010)"],
    "atraxi": ["The Eleventh Hour (2008)"],
    "smilers": ["The Beast Below (2010)"],
    "Dream Lord": ["Amy's Choice (2010)"],
    "silurians": ["The Hungry Earth (2010)", "Cold Blood (2010)"],
    "krafayis": ["Vincent and The Doctor (2010)"],
    "sycorax": ["The Pandorica Opens (2010)"]

    
    

}   

ep_search = input("Search a villain: ").lower()

if ep_search in enemies:
    print(f"{ep_search.title()} appears in: {', '.join(enemies[ep_search])}")
else:
    print("Enemy not found.")
