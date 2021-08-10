# 配置导入库目录
import traci
import sys
import time
import os

def getEEBLr(speed, reactionTime, deceleration, safetyFactor):
    return speed*reactionTime+safetyFactor*(speed**2)/2/deceleration

def isDangerTTC(v_ego,v_0,range):
    '''
    设定阈值
    '''
    return True if range / (v_ego - v_o) <= 2.7 else False

def praseContext(dict):
    return dict[64],dict[66],dict[80],dict[82]


if __name__ == '__main__':
    # 配置调用目录
    try:
        SUMO_HOME = os.environ.get('SUMO_HOME')
    except:
        print('配置SUMO环境')
    else:
        sys.path.append(SUMO_HOME+'/tools/')
        sumoBinary = SUMO_HOME+"/bin/sumo-gui"
        sumoCmd = [sumoBinary, "-c", r'0009.sumocfg']

        # 导入traci模块
        traci.start(sumoCmd)
        collisionVehList = set()
        vehInfo = {
                    '1': {'id': '1', 'speed': 10},
                    }
        step = 0
        while traci.simulation.getMinExpectedNumber() > 0:
            print('step:', step)
            try:
                for veh in vehInfo.values():
                    traci.vehicle.setSpeedMode(veh['id'], 0)                # 禁用速度模型
                    traci.vehicle.setLaneChangeMode(veh['id'], 0)           # 禁用换道
                    traci.vehicle.setSpeed(veh['id'], veh['speed'])         # 设置固定速度
            except:
                pass
            traci.simulationStep()
            if traci.simulation.getCollidingVehiclesNumber() > 0:
                collisionVeh = set(traci.simulation.getCollidingVehiclesIDList())
                collisionVehList.update(collisionVeh)
                for keys in vehInfo:
                    if keys in collisionVeh:
                        vehInfo[keys]['speed'] = 0
                        traci.vehicle.setColor(keys, (255, 0, 0))
                        time.sleep(10)
                        traci.close()
            print('事故车辆：', collisionVehList)
            step += 1