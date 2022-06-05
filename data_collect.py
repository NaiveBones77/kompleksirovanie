import serial
import csv


def collect(fs, duration, filename, plot=False):

    SERIAL_PORT = 'COM3'
    SERIAL_BAUD = 9600
    OUT_FILE = filename


    ts = 1.0 / fs  # Sample period [s]
    samples = int(duration * fs) # Number of samples to record

    ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)

    with open(OUT_FILE, newline='', mode='w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        t = 0
        for _ in range(samples):
                try:
                    # Read serial stream and extract data
                    dataList = ser.readline().decode('utf-8').strip('\r\n').split(' ')
                    dataList.append(t)
                    # Write data to CSV file: gx,gy,gz
                    csvwriter.writerow(dataList)
                    t += ts
                except:
                    pass



collect(54, 130, 'accel_data_zero130.csv')