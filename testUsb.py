import pyvisa
import time

def main():
    # Initialize the resource manager
    rm = pyvisa.ResourceManager()

    # Find and open the USB device
    resources = rm.list_resources()
    print("Available VISA resources:", resources)

    # Assuming the first device is the monochromator
    device_address = resources[0]
    print(f"Connecting to device at {device_address}")
    
    device = rm.open_resource(device_address)
    
    # Set a longer timeout for the device
    device.timeout = 60000  # 60 seconds

    # List of wavelengths to set
    wavelengths = [450.0, 525.0, 600.0]

    command = "gowave 450.0"

    device.write(command)

    time.sleep(10)

    command = "gowave 525.0"

    device.write(command)

    time.sleep(10)


    # for wavelength in wavelengths:
    #     command = f"gowave {wavelength}"
    #     print(f"Sending command: {command}")
    #     device.write(command)
        
    #     # Wait for the operation to complete with retry mechanism
    #     while True:
    #         try:
    #             device.query("*opc?")
    #             break
    #         except pyvisa.errors.VisaIOError as e:
    #             print(f"Timeout error: {e}. Retrying...")
        
    #     # Wait for 15 seconds before changing to the next wavelength
    #     time.sleep(15)

    # Close the device connection
    device.close()
    rm.close()

if __name__ == "__main__":
    main()
