# 配置导入库目录
import traci
import sys
import os
import time

def isPedestrianBeenHit(vehPos, pedPos, vehLength, vehWidth):
    #if 机动车从东向西
    vehUp = vehPos[1] + vehWidth / 2
    vehDown = vehPos[1] - vehWidth / 2
    vehRight = vehPos[0] + 1
    vehLeft = vehPos[0] - vehLength - 1
    return True if pedPos[0]>vehLeft and pedPos[0]<vehRight and pedPos[1]>vehDown and pedPos[1]<vehUp else False

def isInDanger(v1, v2, range,):
    '''
    TTC阈值去判断是否危险？
    '''
    TTC = 4
    if  ttc<TTC:
        return('危险--->规避')
    else
        read

if __name__ == '__main__':
    # 配置调用目录
    try:
        SUMO_HOME = os.environ.get('SUMO_HOME')
    except:
        print('配置SUMO环境')
    else:
        sys.path.append(SUMO_HOME+'/tools/')
        sumoBinary = SUMO_HOME+"/bin/sumo-gui"
        sumoCmd = [sumoBinary, "-c", r'veh_Running_Red_Light.sumocfg']

        # 导入traci模块
        traci.start(sumoCmd)
        collisionTag = False
        vehInfo = {
                    '0': {'id': '0', 'speed': 10}
                    }
        step = 0
        while traci.simulation.getMinExpectedNumber() > 0:
            print('>>> step:', step)
            try:
                for veh in vehInfo.values():
                    traci.vehicle.setSpeedMode(veh['id'], 0)                # 禁用速度模型
                    traci.vehicle.setLaneChangeMode(veh['id'], 0)           # 禁用换道
                    traci.vehicle.setSpeed(veh['id'], veh['speed'])         # 设置固定速度
            except:
                pass
            
            t
            # 判断车辆是否危险panduan cheliangshig
            if weixian :
                fangzhaung chuoshi .。。traci控制
            else:
                traci.simulationStep()
                traci.vehicle.setde('0', )
                if isPedestrianBeenHit(traci.vehicle.getPosition('0'), traci.person.getPosition('ped0'), traci.vehicle.getLength('0'), traci.vehicle.getWidth('0')):
                    collisionTag = True
                    collisionVeh = set(['0'])
                    print('事故车辆：', collisionVeh)
                    for keys in vehInfo:
                        if keys in collisionVeh:
                            vehInfo[keys]['speed'] = 0
                            traci.vehicle.setColor(keys, (255, 0, 0))
                            time.sleep(10)
                            traci.close()
                # if collisionTag:
                #     print('行人停止')
                #     traci.person.setSpeed('ped0', 0)
            

            step += 1