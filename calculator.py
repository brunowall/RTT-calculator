import math
import sys
def calcula_rtt():
	num_rtt = int(raw_input("Digite o numero de RTTS"+"\n"))
	rttinit =  float(raw_input("Digite o RTT incial"+"\n"))
	

	media = rttinit
	desvio = 0.0
	if num_rtt == 1:
		print("Media inicial: " + str(rttinit) + " ") 
		print("Desvio inicial: " + str(0.0) + "\n")
		sys.exit(0)


	for i in range (2,num_rtt+1):
		rttatual = float(raw_input("Digite o proximo RTT "))
		
	
		media  = 0.875*media + 0.125*rttatual
		desvio = 0.75*desvio + 0.25 * fabs(rttatual - media)
		print("Media = "+ str(0.875)+" * media"+" + " +"0.125 "  + " * " + str(rttatual) + " = " + str(media) + " ")
		print("desvio = "+ "0.75" + " * "+"desvio" + " + " + " 0.25" + " * |media -  rtt| = "   + str(desvio)+"\n")




calcula_rtt();