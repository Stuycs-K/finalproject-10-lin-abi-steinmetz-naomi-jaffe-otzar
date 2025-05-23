encode:
	@python3 lsb/encode.py $(ARGS)
encode2:
	@python lsb/encode.py
decode:
	@python3 lsb/decode.py $(ARGS)
decode2:
	@python lsb/decode.py $(ARGS)
