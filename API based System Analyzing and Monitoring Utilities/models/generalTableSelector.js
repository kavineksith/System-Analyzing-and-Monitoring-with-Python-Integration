const db = require('../database.js');

const GeneralTableSelector = (section) => {
    let query;
    switch (section) {
        case 'DeviceBattery':
            query = `SELECT * FROM batteryManagement`;
            break;
        case 'DeviceCPU':
            query = `SELECT * FROM CPUManagementStatistics`;
            break;
        case 'DeviceNetwork':
            query = `SELECT * FROM networkManagement`;
            break;
        case 'DevicePartitions':
            query = `SELECT * FROM PartitionsManagementTable`;
            break;
        case 'DevicePartitionsStatus':
            query = `SELECT * FROM PartitionsAnalyzedReports`;
            break;
        case 'DeviceVMMemory':
            query = `SELECT * FROM virtualMemoryManagement`;
            break;
        case 'DeviceSWMemory':
            query = `SELECT * FROM swapMemoryManagement`;
            break;
        case 'DeviceUsers':
            query = `SELECT * FROM UserManagement`;
            break;
        case 'DeviceInfo':
            query = `SELECT * FROM DeviceInformation`;
            break;
        default:
            break;
    }
    return query;
};

module.exports = GeneralTableSelector;
