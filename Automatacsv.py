import pandas as pd

class automataFD:
  
  def __init__(self):  # Constructor corregido
    self.leerAutomata()
    self.Q = self.definir_estados()  # conjunto de estados es objeto series
    self.SIGMA = self.definir_alfabeto()
    self.DELTA = self.definir_transicion()
    self.START_STATE, self.ACCEPT_STATES = self.set_start_accept()
    self.EstadoActual = None
  
  def leerAutomata(self):
    """Se obtiene el autómata en bruto del csv"""
    self.dataFrameAutomata = pd.read_csv('pruebaAutomata.csv')
    # limpiamos los nulos para trabajar sobre valores reales
    self.dataFrameAutomata = self.dataFrameAutomata.dropna()

  # dataFrameAutomata NO CAMBIARÁ A PARTIR DE AHORA
  def definir_estados(self):
    Q_in = self.dataFrameAutomata.iloc[:, 0] 
    print(f"STATES:\n {Q_in}")
    return Q_in 
      
  def set_start_accept(self):
    while True:
      start = input("Dame el estado inicial del Autómata: ")
      accept = input('Dame el o los estados de aceptación: ').split()
      # Asegurarse de que los estados proporcionados por el usuario son válidos
      if (start in self.Q) and (set(accept).issubset(set(self.Q))):
        return start, accept
      else:
        print(f"Favor de proporcionar estados inicial y finales válidos que deben estar en Q: {self.Q}.")

  def definir_alfabeto(self):
    SIGMA_in = input("Dame el alfabeto del autómata, separados por espacios en blanco: ").split()
    print(f"ALPHABET: {SIGMA_in}")
    return SIGMA_in

  def definir_transicion(self):
    transi_dict = {q: {a: "JACHI" for a in self.SIGMA} for q in self.Q}

    for key, dic_val in transi_dict.items():
      print(f"Estoy en el estado {key}. ESCRIBIR JACHI SI NO EXISTE ESTADO DE TRANSICION.")
      for alphabet_in in dic_val:
        transi_dict[key][alphabet_in] = input(f"Estoy en {key} y veo {alphabet_in}, ¿a qué estado voy?: ")

    print("TRANSITION FUNCTION Q X SIGMA --> Q")
    print("CURRENT STATE  \t INPUT ALPHABET \t NEXT STATE")

    for key, dic_val in transi_dict.items():
      for alphabet_in, transi_state in dic_val.items():
        print(f"\t{key}\t{alphabet_in}\t{transi_state}")
    return transi_dict
  
  def checar_estado_aceptacion(self):
    return self.EstadoActual in self.ACCEPT_STATES

  def recorrer_automata(self, w):
    """Recorrer el autómata para ver si w llega a un estado final"""
    self.EstadoActual = self.START_STATE

    for x in w:
      # Validar si la entrada está en el alfabeto
      if x not in self.SIGMA:
        print(f"Símbolo '{x}' no está en el alfabeto SIGMA.")
        return False

      verificar_estado = self.DELTA[self.EstadoActual][x]
      if verificar_estado == 'JACHI':
        return False

      # Actualizar el estado actual
      self.EstadoActual = verificar_estado

    # Verificar si se llega a un estado de aceptación
    return self.checar_estado_aceptacion()

if __name__ == "__main__":  # Condición corregida
  print("Autómata de estado finito determinista")
  
  m = None  # Variable para almacenar el autómata actual
  while True:
    print("a) Crear un nuevo autómata")
    print("b) Probar una cadena en el autómata")
    print("c) Salir")
    
    opcion = input("Seleccione una opción: ").lower()
    
    if opcion == "a":
      # Crear un nuevo autómata
      m = automataFD()
      print("Nuevo autómata creado exitosamente.")
    
    elif opcion == "b":
      # Probar una cadena en el autómata
      if m is None:
        print("Primero debe crear un autómata (opción a).")
      else:
        input_w = input("Proporcione su cadena: ")
        print("Cadena Aceptada" if m.recorrer_automata(input_w) else "Cadena rechazada")
    
    elif opcion == "c":
      print("Saliendo del programa...")
      break
    else:
      print("Opción no válida. Por favor, seleccione 'a', 'b' o 'c'.")
