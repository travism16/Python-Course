from getpass import getpass

password = getpass()

cisco3 = dict(
	hostname="cisco3.lasthop.io",
	device_type="ios",
	username="pyclass",
	password=password,
	optional_args={},
)

arista1 = dict(
	hostname="arista1.lasthop.io",
	device_type="eos",
	username="pyclass",
	password=password,
	optional_args={},
)

all_devices = [cisco3, arista1]
