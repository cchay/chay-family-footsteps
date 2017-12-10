import random

class Weapon( ):
    def __init__( self ):
        self.Sword = 'sword'
        self.Mace = 'mace'
        self.Knife = 'knife'
        self.Spear = 'spear'

    def GetSword( self ):
        return self.Sword

    def SetSword( self ):
        self.Sword = Sword

    def GetMace( self ):
        return self.Mace

    def SetMace( self ):
        self.Mace = Mace

    def GetKnife( self ):
        return self.Knife

    def SetSpear( self ):
        self.Spear = Spear





    def GetWeapon( self, Weapon ):
        self.Sword( Sword )
        self.Mace( Mace )
        self.Knife( Knife )
        self.Spear( Spear )




    def GenerateWeaponDamage( self ):
        if Weapon == "Sword":
            return random.randint( 1, 7 )
        if Weapon == "Mace":
            return random.randint( 1, 5 )
        if Weapon == "Knife":
            return random.randint( 1, 2 )
        if Weapon == "Spear":
            return random.randint( 1, 10 )

    
