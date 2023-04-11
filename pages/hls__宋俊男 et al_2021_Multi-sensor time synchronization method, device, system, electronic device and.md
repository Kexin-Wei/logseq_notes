file:: [宋俊男 et al_2021_Multi-sensor time synchronization method, device, system, electronic device and.pdf](file://D:/Dropbox/Study/ZoteroFiles/宋俊男 et al_2021_Multi-sensor time synchronization method, device, system, electronic device and.pdf)
file-path:: file://D:/Dropbox/Study/ZoteroFiles/宋俊男 et al_2021_Multi-sensor time synchronization method, device, system, electronic device and.pdf

- [:span]
  ls-type:: annotation
  hl-page:: 13
  hl-color:: yellow
  id:: 63b3866e-2659-4d65-aa05-d954edcaa368
  hl-type:: area
  hl-stamp:: 1672709739384
- 多传感器时间同步系统，可以用于至少三大类多个传感器的时间同步
  ls-type:: annotation
  hl-page:: 6
  hl-color:: yellow
  id:: 63b386ae-246c-408a-acce-d0dbd6ab7336
- 上位机可以是各类PC主机，也可以是基于嵌入式芯片的硬件平台 ，本实施例中以基于Linux系统的工控主机为例
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b386da-c771-45af-9520-8ecec3a81342
- 时间主控设备可以是MCU、DSP或 FPGA等嵌入式平台，在本实施例中以STM32单片机系统为例
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b386e3-e580-450f-a21f-e58c82875503
- 时间主控设备和上位机之间采用 RS232串行接口通信，波特率最大可达到921600bps，时间主控设备通过该串口接收上位机授时，获得授时时刻的微秒级时间戳存入寄存器中，以作为时间同步系统的起始时间
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b3870c-e699-47ad-83c3-989f6e967e3c
- 为了使整个时间同步系统具有一致的起始时间，根据与上位机间的硬件接口类型，设计接口通信驱动，接收由上位机生成的初始时间戳，其中，所述初始时间戳是由上位机读取计算机系统内部时间获得的
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b38721-5892-4907-9204-5849d87f4020
- 对于没有内部时钟的传感器，时间主控设备生成的内部时间戳可以看作传感器采集数据的精确时间，用来和系统中其他传感器时间同步
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b387cd-8a4d-4f42-9a71-9c16cb881c01
- 具体地，接收到上位机发送的初始时间戳后，开启用于累加计时的内部定时器T1，所述内部定时器T1的频率是以硬件系统中挂载的固定频率高精度晶振为基准，通过倍频得到的。通过对所述定时器T1的配置，使其在累加计数一段时间t0后溢出并重新计数，并将t0累加到接收到的初始时间戳，以此获得不断更新的内部时间戳
  ls-type:: annotation
  hl-page:: 7
  hl-color:: yellow
  id:: 63b387e6-d915-493f-9705-84d8ab571b19
- 第二传感器表示有内部时钟的传感器，可以根据秒脉冲同步信号与时间主控设备计时同步，也可以根据触发脉冲信号进行外触发模式下的数据采集。此类传感器以IMU为例
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b3883c-486d-403d-a593-2df35eb10a26
- 第三传感器表示不支持根据秒脉冲信号计时同步，但支持根据触发脉冲信号进行触发数据采集的传感器，此类传感器以相机为例
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b3884f-7e76-41cb-89e7-04719a429a43
- 通过与上位机之间的RS232串行通信接口，将所述内部时间戳和触发脉冲的计数值按照f1的频率发送给上位机。所述内部时间戳和触发脉冲计数值用于在上位机端和所述第三传感器的数据进行匹配。上位机从第三传感器得到一组数据帧计数值，通过对两组计数的匹配，可以使所述第三传感器的每一帧数据都匹配一组对应于数据采集时刻的时间戳。
  ls-type:: annotation
  hl-page:: 8
  hl-color:: yellow
  id:: 63b38894-c22b-4d63-bb69-8c128ae7292a