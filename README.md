# coldp2scan

coldp2scan to converts Catalogue of Life data package (CoLDP) format into SCAN format.

# Use
1) Git clone this repo:
```
git clone https://github.com/gdower/coldp2scan.git
```
2) Place the CoLDP zip file in the raw directory
3) Run the following command (with the `--abort-on-container-exit` to terminate the database after conversion finishes):
```
docker-compose up --abort-on-container-exit
```
4) The output will be in the scan directory.

# Requirements
Docker