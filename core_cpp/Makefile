CXX = g++
CXXFLAGS = -O3 -shared -fPIC

TARGET = libquantum_engine.so
SRC = quantum_engine.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)
