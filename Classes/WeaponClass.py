class Thing(  ):
   def __init__( self ):
      self._ID = ''
      self._Name = ''
      self._Type = ''
      self._Description = ''
      self._Weight = 0
      self._Price = 0




   def GetID( self ):
      return self._ID

   def SetID( self, ID ):
      self._ID = ID


   def GetName( self ):
      return self._Name

   def SetName( self, Name ):
      self._Name = Name


   def GetType( self ):
      return self._Type

   def SetType( self, Type ):
      self._Type = Type


   def GetDescription( self ):
      return self._Description

   def SetDescription( self, Description ):
      self._Description = Description


   def GetWeight( self ):
      return self._Weight

   def SetWeight( self, Weight ):
      self.Weight = Weight


   def GetPrice( self ):
      return self._Price

   def SetPrice( self, Price ):
      self._Price = Price




class Weapon( Thing ):
   def Weapon( self, ID, Name, Type, Description, Price ):
      self.SetID( ID )
      self.SetName( Name )
      self.SetType( Type )
      self.SetDescription( Description )
      self.SetPrice( Price )
      self.SetSpeed = 0
      self.SetDamage = 0
      self._HitRollMod = 0

   def GetSpeed( self ):
      return self._Speed

   def SetSpeed( self, Speed ):
      self._Speed = Speed


   def GetDamage( self ):
      return self._Damage

   def SetDamage( self, Damage ):
       self._Damage = Damage


   def GetHitRollMod( self ):
       return self._HitRollMod

   def SetHitRollMod( self, HitRollMod ):
      self._HitRollMod = HitRollMod





class Armour( Thing ):
   def Armour( self, ID, Name, Type, Description, Price ):
      self.SetID( ID )
      self.SetName( Name )
      self.SetType( Type )
      self.SetDescription( Description )
      self.SetPrice( Price )
      self._AC = 0

   def GetAC( self ):
      return self._AC

   def SetAC( self, AC ):
      self._AC = AC






class Regenerator( Thing ):
   def Regenerator( self, ID, Name, Type, Description, Price ):
      self.SetID( ID )
      self.SetName( Name )
      self.SetType( Type )
      self.SetDescription( Description )
      self.SetPrice( Price )
      self._HPRestore = 0

   def GetHPRestore( self ):
      return self._HPRestore

   def SetHPRestore( self, HPRestore ):
      self._HPRestore = HPRestore

