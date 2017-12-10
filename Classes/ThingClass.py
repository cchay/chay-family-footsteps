class Thing(  ):
   def __init__( self ):
      self.__ID = ''
      self.__Name = ''
      self.__Type = ''
      self.__Description = ''
      self.__Weight = 0
      self.__Price = 0




   def GetID( self ):
      return self.__ID

   def SetID( self, ID ):
      self.__ID = ID


   def GetName( self ):
      return self.__Name

   def SetName( self, Name ):
      self.__Name = Name


   def GetType( self ):
      return self.__Type

   def SetType( self, Type ):
      self.__Type = Type


   def GetDescription( self ):
      return self.__Description

   def SetDescription( self, Description ):
      self.__Description = Description


   def GetWeight( self ):
      return self.__Weight

   def SetWeight( self, Weight ):
      self.__Weight = Weight


   def GetPrice( self ):
      return self.__Price

   def SetPrice( self, Price ):
      self.__Price = Price




class Weapon( Thing ):
   def Weapon( self, ID, Name, Type, Description, Price ):
      self.SetID( ID )
      self.SetName( Name )
      self.SetType( Type )
      self.SetDescription( Description )
      self.SetPrice( Price )
      self.SetSpeed = 0
      self.SetDamage = 0
      self.__HitRollMod = 0

   def GetSpeed( self ):
      return self.__Speed

   def SetSpeed( self, Speed ):
      self.__Speed = Speed


   def GetDamage( self ):
      return self.__Damage

   def SetDamage( self, Damage ):
       self._Damage = Damage


   def GetHitRollMod( self ):
       return self.__HitRollMod

   def SetHitRollMod( self, HitRollMod ):
      self.__HitRollMod = HitRollMod





class Armour( Thing ):
   def Armour( self, ID, Name, Type, Description, Price ):
      self.SetID( ID )
      self.SetName( Name )
      self.SetType( Type )
      self.SetDescription( Description )
      self.SetPrice( Price )
      self.__AC = 0

   def GetAC( self ):
      return self.__AC

   def SetAC( self, AC ):
      self.__AC = AC






class Regenerator( Thing ):
   def Regenerator( self, ID, Name, Type, Description, Price ):
      self.SetID( ID )
      self.SetName( Name )
      self.SetType( Type )
      self.SetDescription( Description )
      self.SetPrice( Price )
      self.__HPRestore = 0

   def GetHPRestore( self ):
      return self.__HPRestore

   def SetHPRestore( self, HPRestore ):
      self.__HPRestore = HPRestore

