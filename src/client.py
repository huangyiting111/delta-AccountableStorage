import zmq

class RpcPdrClient(object):
    
    def __init__(self, context):
        self.context = context
    
    def rpc(self, ip, port, msg):
        sock = self.context.socket(zmq.REQ)
        sock.connect("tcp://"+str(ip)+":"+str(port))
        sock.send(msg)
        
        inMsg = sock.recv()
        sock.close()
        return inMsg
        

