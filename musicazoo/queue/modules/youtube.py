import musicazoo.queue.module as module
import musicazoo.lib.packet as packet

if __name__ != '__main__':
    class Youtube(module.Module):
        TYPE_STRING='youtube'
        process = ['python',__file__]

else: # name is main
    conn=module.ParentConnection()

    def poller():
        while True:
            print conn.recv_cmd()
            conn.send_resp(packet.good())

    import sys
    import threading

    t=threading.Thread(target=poller)
    t.daemon=True
    t.start()

    import time
    time.sleep(4)
    print "QUITTING"
    conn.close()