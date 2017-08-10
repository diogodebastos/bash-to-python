import sys
import getopt

# Placeholder variables
maxFom = 7.8
cutFom = 8.3

for eachArg in sys.argv[0:]:
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hn:l:', ['help','nodes','layers'])
        #opts, args = getopt.getopt(sys.argv[1:])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "Help"
            sys.exit()
        elif opt in ("-n", "--nodes"):
            nodes = arg
            #print(arg)
        elif opt in ("-l", "--layers"):
            layers = arg
            #print(arg) 

print "\t# Layers: " + layers + "\n\t# Nodes: " + nodes + "\n\tMax Fom: " + str(maxFom) + " at cut " + str(cutFom)

layers = float(layers)
nodes = float(nodes)
