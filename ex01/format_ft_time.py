import datetime
import time

now = datetime.datetime.now()
time_coma = "{:,}".format(time.time())
seconds = time.time()

print("Seconds since January 1, 1970:", time_coma, "or", f"{seconds:.2e}", "in scientific notation")
print(now.strftime("%b %d %Y"))

# expected output:
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$