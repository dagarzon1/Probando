fecha_manchas.pdf: grafica.py fecha_mancha.dat
	python grafica.py

fecha_mancha.dat: procesa.py monthrg.dat
	python procesa.py

monthrg.dat:
	wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/solar/monthrg.dat
