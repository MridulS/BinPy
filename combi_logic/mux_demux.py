import sys
from PyIC import Gates

class MUX:
	def __init__(self):
		self.gates = Gates()

	def run(self,inputs,select_inputs,strobe=1):
		allowed = [2,4,8,16,32]
		mux_type = len(inputs)
		if mux_type not in allowed:
			sys.exit("ERROR: only 5 types of MUX are supported, namely, 2:1, 4:1, 8:1, 16:1 and 32:1")
		if 2**len(select_inputs)!=mux_type:
			sys.exit("ERROR: no of select inputs do not comply with no of inputs")
		if mux_type == 2:
			return self.mux_2_1(inputs,select_inputs,strobe)
		elif mux_type == 4:
			return self.mux_4_1(inputs,select_inputs,strobe)
		elif mux_type == 8:
			return self.mux_8_1(inputs,select_inputs,strobe)

	def mux_2_1(self,inputs,select_inputs,strobe=1):
		s = select_inputs[0]
		a = inputs[0]
		b = inputs[1]
		result = self.gates.OR(self.gates.AND(a,self.gates.NOT(s)),self.gates.AND(b,s))
		if strobe==1:
			return result
		else:
			return self.gates.NOT(result)

	def mux_4_1(self,inputs,select_inputs,strobe=1):
		s0 = select_inputs[0]
		s1 = select_inputs[1]
		a,b,c,d = inputs[0],inputs[1],inputs[2],inputs[3]
		term1 = self.gates.AND(a,self.gates.NOT(s0),self.gates.NOT(s1))
		term2 = self.gates.AND(b,s0,self.gates.NOT(s1))
		term3 = self.gates.AND(c,self.gates.NOT(s0),s1)
		term4 = self.gates.AND(d,s0,s1)
		result = self.gates.OR(term1,term2,term3,term4)
		if strobe==1:
			return result
		else:
			return self.gates.NOT(result)

	def mux_8_1(self,inputs,select_inputs,strobe=1):
		s0 = select_inputs[0]
		s1 = select_inputs[1]
		s2 = select_inputs[2]
		a,b,c,d,e,f,g,h = inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7]
		term1 = self.gates.AND(a,self.gates.NOT(s2),self.gates.NOT(s1),self.gates.NOT(s0)
		term2 = self.gates.AND(b,self.gates.NOT(s2),self.gates.NOT(s1),s0)
		term3 = self.gates.AND(c,self.gates.NOT(s2),s1,self.gates.NOT(s0))
		term4 = self.gates.AND(d,self.gates.NOT(s2),s1,s0)
		term5 = self.gates.AND(e,s2,self.gates.NOT(s1),self.gates.NOT(s0))
		term6 = self.gates.AND(f,s2,self.gates.NOT(s1),s0)
		term7 = self.gates.AND(g,s2,s1,self.gates.NOT(s0))
		term8 = self.gates.AND(h,s2,s1,s0)
		result = self.gates.OR(term1,term2,term3,term4,term5,term6,term7,term8)
		if strobe==1:
			return result
		else:
			return self.gates.NOT(result)