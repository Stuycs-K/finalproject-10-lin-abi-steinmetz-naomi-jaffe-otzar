encode:
	@python3 lsb/encode.py
encode2:
	@python lsb/encode.py
decode:
	@python3 lsb/decode.py $(ARGS)
decode2:
	@python lsb/decode.py $(ARGS)
compare:
	@python3 lsb/audioQuality.py $(ARGS)
compare2:
	@python lsb/audioQuality.py $(ARGS)
encode_phase:
	@python3 phase/encode.py $(ARGS)
encode_phase2:
	@python phase/encode.py $(ARGS)
decode_phase:
	@python3 phase/decode.py $(ARGS)
decode_phase2:
	@python phase/decode.py $(ARGS)