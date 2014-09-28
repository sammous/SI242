virus=open("virus.txt","rb")

liste_instruction=[]      # liste des instructions en assembleur

for line in virus:
    a,b,c=line.split(' ',2)
    liste_instruction.append(b)

virus.close()

print(liste_instruction)

liste_contrabass=[]
liste_cello=[]
liste_violin=[]
liste_trumpet=[]
liste_clarinet=[]
liste_bassoon=[]
liste_oboe=[]
liste_taiko=[]
liste_celesta=[]
liste_ocarina=[]

liste_instrument = [('Ocarina',liste_ocarina,'79'),('Celesta',liste_celesta,'8'),('Taiko',liste_taiko,'116'),('Contrabass',liste_contrabass,'43'),('Cello',liste_cello,'42'),('Violin',liste_violin,'40'),('Trumpet',liste_trumpet,'56'),('Clarinet',liste_clarinet,'71'),('Bassoon',liste_bassoon,'70'),('Oboe',liste_oboe,'68')]

Dico={}

# Data transfert instructions

Dico['bswap']=('A,','Contrabass')
Dico['cbw']=('B,','Contrabass')
Dico['cdq']=('C','Contrabass')
Dico['cdqe']=('D','Contrabass')
Dico['cmova']=('E','Contrabass')
Dico['cmovae']=('F','Contrabass')
Dico['cmovb']=('G','Contrabass')
Dico['cmovbe']=('A','Contrabass')
Dico['cmovc']=('B','Contrabass')
Dico['cmove']=('c','Contrabass')
Dico['cmovg']=('d','Contrabass')
Dico['cmovge']=('e','Contrabass')
Dico['cmovl']=('f','Contrabass')
Dico['cmovle']=('g','Contrabass')
Dico['cmovna']=('a','Contrabass')
Dico['cmovnae']=('b','Contrabass')
Dico['cmovnb']=('c\'','Contrabass')
Dico['cmovnbe']=('d\'','Contrabass')
Dico['cmovnc']=('A,','Cello')
Dico['cmovne']=('B,','Cello')
Dico['cmovng']=('C','Cello')
Dico['cmovnge']=('D','Cello')
Dico['cmovnl']=('E','Cello')
Dico['cmovnle']=('F','Cello')
Dico['cmovno']=('G','Cello')
Dico['cmovnp']=('A','Cello')
Dico['cmovns']=('B','Cello')
Dico['cmovnz']=('c','Cello')
Dico['cmovo']=('d','Cello')
Dico['cmovp']=('e','Cello')
Dico['cmovpe']=('f','Cello')
Dico['cmovpo']=('g','Cello')
Dico['cmovs']=('a','Cello')
Dico['cmovz']=('b','Cello')
Dico['cmpxchg8b']=('c\'','Cello')
Dico['cqo']=('d\'','Cello')
Dico['cwd']=('A,','Violin')
Dico['cwde']=('B,','Violin')
Dico['mov']=('C','Violin')
Dico['movabs']=('D','Violin')
Dico['movsx']=('E','Violin')
Dico['movzx']=('F','Violin')
Dico['pop']=('G','Violin')
Dico['popa']=('A','Violin')
Dico['popad']=('B','Violin')
Dico['push']=('c','Violin')
Dico['pusha']=('d','Violin')
Dico['pushad']=('e','Violin')
Dico['xadd']=('f','Violin')
Dico['xchg']=('g','Violin')
Dico['pushfd']=('a','Violin')

# Binary Arithmetic Instructions:

Dico['adc']=('A,','Trumpet')
Dico['add']=('B,','Trumpet')
Dico['cmp']=('C','Trumpet')
Dico['dec']=('D','Trumpet')
Dico['div']=('E','Trumpet')
Dico['idiv']=('F','Trumpet')
Dico['imul']=('G','Trumpet')
Dico['inc']=('A','Trumpet')
Dico['mul']=('B','Trumpet')
Dico['neg']=('c','Trumpet')
Dico['sbb']=('d','Trumpet')
Dico['sub']=('e','Trumpet')

# Control Transfert Instructions:

Dico['bound']=('A,','Clarinet')
Dico['call']=('B,','Clarinet')
Dico['enter']=('C','Clarinet')
Dico['int']=('D','Clarinet')
Dico['into']=('E','Clarinet')
Dico['iret']=('F','Clarinet')
Dico['ja']=('G','Clarinet')
Dico['jae']=('A','Clarinet')
Dico['jb']=('B','Clarinet')
Dico['jbe']=('c','Clarinet')
Dico['jc']=('d','Clarinet')
Dico['jcxz']=('e','Clarinet')
Dico['je']=('f','Clarinet')
Dico['jecxz']=('g','Clarinet')
Dico['jg']=('a','Clarinet')
Dico['jge']=('b','Clarinet')
Dico['jl']=('c\'','Clarinet')
Dico['jle']=('d\'','Clarinet')
Dico['jmp']=('A,','Bassoon')
Dico['jnae']=('B,','Bassoon')
Dico['jnb']=('C','Bassoon')
Dico['jnbe']=('D','Bassoon')
Dico['jnc']=('E','Bassoon')
Dico['jne']=('F','Bassoon')
Dico['jng']=('G','Bassoon')
Dico['jnge']=('A','Bassoon')
Dico['jnl']=('B','Bassoon')
Dico['jnle']=('c','Bassoon')
Dico['jno']=('d','Bassoon')
Dico['jnp']=('e','Bassoon')
Dico['jns']=('f','Bassoon')
Dico['jnz']=('g','Bassoon')
Dico['jo']=('a','Bassoon')
Dico['jp']=('b','Bassoon')
Dico['jpe']=('c\'','Bassoon')
Dico['jpo']=('d\'','Bassoon')
Dico['js']=('A,','Oboe')
Dico['jz']=('B,','Oboe')
Dico['call']=('C','Oboe')
Dico['leave']=('D','Oboe')
Dico['loop']=('E','Oboe')
Dico['loope']=('F','Oboe')
Dico['loopne']=('G','Oboe')
Dico['loopnz']=('A','Oboe')
Dico['ret']=('B','Oboe')

# Miscellaneous instructions

Dico['lea']=('B,','Taiko')
Dico['nop']=('C','Taiko')

# Logical instructions

Dico['and']=('A,','Celesta')
Dico['not']=('B,','Celesta')
Dico['or']=('C','Celesta')
Dico['xor']=('D','Celesta')

# Bit and Byte instructions

Dico['setnz']=('A,','Ocarina')
Dico['test']=('a','Ocarina')

partition=open("partition.txt","wb")

# en tÃªte de la partition

partition.write('X:1\n')
partition.write("T:Partition Virus\n")
partition.write('M:4/4\n')
partition.write('K:G\n')

# écriture d'une fonction pour la constitution des listes de notes par instruments

def transcription(liste_instrument,instruction,Dico):
    for i in liste_instrument:
        if i[0]==Dico.get(instruction,('',''))[1]:
            i[1].append(Dico[instruction][0])
            for j in liste_instrument:
                if i!=j:
                    j[1].append('z')
            return
    print(instruction)
            
            
# écriture des lises de notes

for i in liste_instruction:
    transcription(liste_instrument,i,Dico)

# on complète la fin de la liste avec des silences

reste=len(liste_instrument[0][1])%4
for i in liste_instrument:
    for j in range(reste):
        i[1].append('z')
        
# écriture de la partition

for i in liste_instrument:
    partition.write('V:'+i[0]+' name='+i[0]+'\n')
    partition.write('%%MIDI program '+i[2]+'\n')
    compteur=1
    for j in i[1]:
        partition.write(j)
        if compteur==4:
            partition.write('|')
            compteur=0
        compteur+=1
    partition.write('||\n')

partition.close()

print(liste_trumpet)
