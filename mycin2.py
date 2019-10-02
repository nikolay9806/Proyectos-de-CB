
import logging
from emycin2 import Parameter, Context, Rule, Shell

#Funciones varias 

def eq(x, y):
    """Function for testing value equality."""
    return x == y

def boolean(string):

    if string == 'True':
        return True
    if string == 'False':
        return False
    raise ValueError('El valor debe ser True o False')


#Datos iniciales, contextos, reglas

def define_contexts(sh1,sh2):
    #Contextos Shell 1 (Sintomas , enfermedad)
    sh1.define_context(Context('sintomas', ['sintoma']))
    sh1.define_context(Context('enfermedades', goals=['enfermedad']))
    
    #Contextos Shell 2 (Enfermedad , tratamiento)
    sh2.define_context(Context('enfermedades', ['enfermedad']))
    sh2.define_context(Context('tratamientos', goals=['tratamiento']))

def define_params(sh1,sh2):
    ## Parametros shell 1
    # Parametros de sintomas 
    sintomas=['fiebre','diarrea','fatiga','dolores musculares','tos','vomito','dificultad para respirar','malestar']
    sh1.define_param(Parameter('sintoma', 'sintomas', enum=sintomas, ask_first=True))
    #Parametros de enfermedad
    enfermedades=['gripa', 'faringitis', 'infeccion intestinal', 'amebas', 'dengue','asma','enfermedad cardiaca']
    sh1.define_param(Parameter('enfermedad', 'enfermedades', enum=enfermedades, ask_first=False))
    
    ## Parametros shell 2
    #Parametros de enfermedad
    sh2.define_param(Parameter('enfermedad', 'enfermedades', enum=enfermedades, ask_first=True))
    #Parametros de tratamiento 
    tratamientos=['acetaminofen','dipirona','ibuprofeno','aspirina','suero 5ml','amoxicilina','salbutamol']
    sh2.define_param(Parameter('tratamiento', 'tratamientos', enum=tratamientos, ask_first=False))


def define_rules(sh1,sh2):
    sh2.define_rule(Rule(1,
                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        [('tratamiento', 'tratamientos', eq, 'acetaminofen')],

                        1))
    sh2.define_rule(Rule(2,
                        [('enfermedad', 'enfermedades', eq, 'faringitis')],

                        [('tratamiento', 'tratamientos', eq, 'dipirona')],

                        1))
    sh2.define_rule(Rule(11,
                        [('enfermedad', 'enfermedades', eq, 'faringitis')],

                        [('tratamiento', 'tratamientos', eq, 'amoxicilina')],

                        1))
    sh2.define_rule(Rule(12,
                        [('enfermedad', 'enfermedades', eq, 'infeccion intestinal')],

                        [('tratamiento', 'tratamientos', eq, 'suero 5ml')],

                        1))
    sh2.define_rule(Rule(13,
                        [('enfermedad', 'enfermedades', eq, 'amebas')],

                        [('tratamiento', 'tratamientos', eq, 'amoxicilina')],

                        1))
    sh2.define_rule(Rule(14,
                        [('enfermedad', 'enfermedades', eq, 'amebas')],

                        [('tratamiento', 'tratamientos', eq, 'suero 5ml')],

                        1))
    sh2.define_rule(Rule(15,
                        [('enfermedad', 'enfermedades', eq, 'dengue')],

                        [('tratamiento', 'tratamientos', eq, 'acetaminofen')],

                        1))
    sh2.define_rule(Rule(16,
                        [('enfermedad', 'enfermedades', eq, 'dengue')],

                        [('tratamiento', 'tratamientos', eq, 'amoxicilina')],

                        1))
    sh2.define_rule(Rule(17,
                        [('enfermedad', 'enfermedades', eq, 'dengue')],

                        [('tratamiento', 'tratamientos', eq, 'ibuprofeno')],

                        1))
    sh2.define_rule(Rule(18,
                        [('enfermedad', 'enfermedades', eq, 'asma')],

                        [('tratamiento', 'tratamientos', eq, 'salbutamol')],

                        1))
    sh2.define_rule(Rule(19,
                        [('enfermedad', 'enfermedades', eq, 'asma')],

                        [('tratamiento', 'tratamientos', eq, 'acetaminofen')],

                        1))
    sh2.define_rule(Rule(20,
                        [('enfermedad', 'enfermedades', eq, 'enfermedad cardiaca')],

                        [('tratamiento', 'tratamientos', eq, 'aspirina')],

                        1))     
    sh1.define_rule(Rule(3,
                        [('sintoma', 'sintomas', eq, 'fiebre')],

                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        0.6))
    sh1.define_rule(Rule(4,
                        [('sintoma', 'sintomas', eq, 'fiebre')],

                        [('enfermedad', 'enfermedades', eq, 'faringitis')],

                        0.3))
    sh1.define_rule(Rule(5,
                        [('sintoma', 'sintomas', eq, 'malestar')],

                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        0.4))
    sh1.define_rule(Rule(6,
                        [('sintoma', 'sintomas', eq, 'malestar')],

                        [('enfermedad', 'enfermedades', eq, 'faringitis')],

                        0.8))
    sh1.define_rule(Rule(7,
                        [('sintoma', 'sintomas', eq, 'diarrea')],

                        [('enfermedad', 'enfermedades', eq, 'infeccion intestinal')],

                        0.6))
    sh1.define_rule(Rule(8,
                        [('sintoma', 'sintomas', eq, 'diarrea')],

                        [('enfermedad', 'enfermedades', eq, 'amebas')],

                        0.7))                     
    sh1.define_rule(Rule(9,
                        [('sintoma', 'sintomas', eq, 'fiebre'),
                        ('sintoma', 'sintomas', eq, 'malestar')],

                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        0.78))
    sh1.define_rule(Rule(10,
                        [('sintoma', 'sintomas', eq, 'fiebre'),
                        ('sintoma', 'sintomas', eq, 'malestar')],

                        [('enfermedad', 'enfermedades', eq, 'faringitis')],

                        0.84))
    sh1.define_rule(Rule(21,
                        [('sintoma', 'sintomas', eq, 'fatiga')],

                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        0.4))
    sh1.define_rule(Rule(22,
                        [('sintoma', 'sintomas', eq, 'fatiga')],

                        [('enfermedad', 'enfermedades', eq, 'enfermedad cardiaca')],

                        0.7))
    sh1.define_rule(Rule(23,
                        [('sintoma', 'sintomas', eq, 'fatiga')],

                        [('enfermedad', 'enfermedades', eq, 'dengue')],

                        0.8))
    sh1.define_rule(Rule(24,
                        [('sintoma', 'sintomas', eq, 'dolores musculares')],

                        [('enfermedad', 'enfermedades', eq, 'dengue')],

                        0.7))
    sh1.define_rule(Rule(25,
                        [('sintoma', 'sintomas', eq, 'dolores musculares')],

                        [('enfermedad', 'enfermedades', eq, 'enfermedad cardiaca')],

                        0.8))
    sh1.define_rule(Rule(26,
                        [('sintoma', 'sintomas', eq, 'tos')],

                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        0.85))
    sh1.define_rule(Rule(27,
                        [('sintoma', 'sintomas', eq, 'tos')],

                        [('enfermedad', 'enfermedades', eq, 'faringitis')],

                        0.75))
    sh1.define_rule(Rule(28,
                        [('sintoma', 'sintomas', eq, 'vomito')],

                        [('enfermedad', 'enfermedades', eq, 'gripa')],

                        0.4))
    sh1.define_rule(Rule(29,
                        [('sintoma', 'sintomas', eq, 'vomito')],

                        [('enfermedad', 'enfermedades', eq, 'dengue')],

                        0.7))
    sh1.define_rule(Rule(30,
                        [('sintoma', 'sintomas', eq, 'dificultad para respirar')],

                        [('enfermedad', 'enfermedades', eq, 'asma')],

                        0.81))
    sh1.define_rule(Rule(31,
                        [('sintoma', 'sintomas', eq, 'dificultad para respirar')],

                        [('enfermedad', 'enfermedades', eq, 'enfermedad cardiaca')],

                        0.6))
    


#Ejecucion del sistema 

def report_findings(findings):
    for inst, result in findings.items():
        print 'Resultados para %s-%d:' % (inst[0], inst[1])
        for param, vals in result.items():
            possibilities = ['%s: %f' % (val[0], val[1]) for val in vals.items()]
            print '%s: %s' % (param, ', '.join(possibilities))
        
if __name__ == "__main__":
    sh1 = Shell()
    sh2 = Shell()
    define_contexts(sh1,sh2)
    define_params(sh1,sh2)
    define_rules(sh1,sh2)
    cont=0
    while(cont==0):
        print ''
        print 'Desea consultar por sintoma o por enfermedad ( S/E)'
        print ''
        res=""
        res=raw_input()
        if res == 'S' or res== 's':    
            report_findings(sh1.execute(['sintomas','enfermedades']))
        elif res== 'E' or 'e':
            report_findings(sh2.execute(['enfermedades','tratamientos']))
        print ''
        print' Desea Continuar? S/N '
        print ''
        res=""
        res=raw_input()
        if res =='N' or res == 'n':
            cont=1