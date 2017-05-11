import math
import sys
def calcula_rtt():
	num_rtt = int(raw_input("Digite o numero de RTTS"))
	rttinit =  float(raw_input("Digite o RTTS incial"))
	

	print("Media inicial: " + str(rttinit) + " ") 
	print("Desvio inicial: " + str(rttinit) + "\n")
	media = rttinit
	desvio = 0.0
	if num_rtt == 1:
		print("Media = ", str(media))
		sys.exit(0)


	for i in range (2,num_rtt+1):
		rttatual = float(raw_input("Digite o proximo RTT "))
		
	
		media  = 0.875*media + 0.125*rttatual
		desvio = 0.75*desvio + 0.25 * fabs(rttatual - media)
		print("Media = "+ str(0.875)+" * media"+" + " +"0.125 "  + " * " + str(rttatual) + " = " + str(media) + " ")
		print("desvio = "+ "0.75" + " * "+"desvio" + " + " + " 0.25" + " * |media -  rtt| = "   + str(desvio)+"\n")




calcula_rtt();