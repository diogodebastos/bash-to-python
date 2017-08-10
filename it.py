import sys
import getopt

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

print "Layers: " + layers + "\n#Nodes: " + nodes 
