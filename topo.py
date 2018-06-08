from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
		 # initilaize topology
		Topo.__init__(self)   
		#add hosts
		host1=self.addHost('h1')
		host2=self.addHost( 'h2' )
		host3=self.addHost('h3')
		host4=self.addHost( 'h4' )
		host5=self.addHost('h5')
		host6=self.addHost( 'h6' )
		host7=self.addHost('h7')
		host8 = self.addHost( 'h8' )
		#add switches
       	 	switch1 = self.addSwitch( 's1' )
        	switch2 = self.addSwitch( 's2' )
        	switch3 = self.addSwitch( 's3' )
        	switch4 = self.addSwitch( 's4' )
		switch5 = self.addSwitch( 's5' )
        	switch6 = self.addSwitch( 's6' )
        	switch7 = self.addSwitch( 's7' )
		#add links
		self.addLink(host1,switch4,1,1)
		self.addLink(host2,switch4,1,2)
		self.addLink(host3,switch5,1,1)
		self.addLink(host4,switch5,1,2)
		self.addLink(host5,switch6,1,1)
		self.addLink(host6,switch6,1,2)
		self.addLink(host7,switch7,1,1)
		self.addLink(host8,switch7,1,2)
        	self.addLink(switch4,switch2,3,1)
       	 	self.addLink(switch5,switch2,3,2)
        	self.addLink(switch6,switch3,3,1)
        	self.addLink(switch7,switch3,3,2)
		self.addLink(switch2,switch1,3,1)
        	self.addLink(switch3,switch1,3,2)

topos = { 'mytopo': ( lambda: MyTopo() ) }
