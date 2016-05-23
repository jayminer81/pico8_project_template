# Pico-8 Project Makefile

LUASOURCE=source.lua
OUTPUT=output.p8
GFXSFX=gfxsfx.p8

output: parse.py head $(LUASOURCE) $(GFXSFX)
	cat head >$(OUTPUT)
	./parse.py $(LUASOURCE) >>$(OUTPUT)
	cat $(GFXSFX) | awk '/__gfx__/ {seen= 1 } seen {print}' >>$(OUTPUT)

clean:
	$(RM) $(OUTPUT)
