function VehicleConstructor(name, wheels, passengers, speed) {
  //AVOIDS BREAKAGE IF CONSTRUCTOR IS CALLED W/O **NEW**
  if (!(this instanceof VehicleConstructor)) {
    return new VehicleConstructor(name, wheels, passengers, speed);
  }
  var _this = this
  //private variables
  var distance_travelled = 0

  //private methods
  function updateDistanceTravelled() {
    distance_travelled += _this.speed;
  }

  //properties
  this.wheels = wheels || 2
  this.speed = speed || 0,
  this.name =  name || 'rollerskates',
  this.passengers = passengers || 0,


  //methods
  this.makeNoise = function(noise) {
    var noise = noise || 'Honk Honk!'
    console.log(noise)
  }
  this.move = function(noise) {
    updateDistanceTravelled();
    this.makeNoise(noise);
  }
  this.checkMiles = function() {
    return distance_travelled;
  }
}

var bus = new VehicleConstructor('Bus', 4, 0, 25);
console.log(bus.checkMiles())
// bus.makeNoise('aergegaer');
bus.move();
console.log(bus.checkMiles())
