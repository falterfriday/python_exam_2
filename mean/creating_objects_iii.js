function VehicleConstructor(name, wheels, passengers, speed) {
  //AVOIDS BREAKAGE IF CONSTRUCTOR IS CALLED W/O **NEW**
  if (!(this instanceof VehicleConstructor)) {
    return new VehicleConstructor(name, wheels, passengers, speed);
  }
  var _this = this
  var distance_travelled = 0

  function updateDistanceTravelled() {
    distance_travelled += _this.speed;
  }

  this.wheels = wheels || 2
  this.speed = speed || 0,
  this.name =  name || 'rollerskates'
  this.passengers = passengers || 0


  this.checkMiles = function() {
    return distance_travelled;
  }
}
//PROTOTYPE - **AVAILABLE TO ALL**
VehicleConstructor.prototype.makeNoise = function(noise) {
  var noise = noise || 'Honk Honk!'
}
VehicleConstructor.prototype.move = function(noise) {
  updateDistanceTravelled();
  this.makeNoise(noise);
}
VehicleConstructor.prototype.checkMiles = function() {
  return distance_travelled;
}
VehicleConstructor.prototype.vin = function() {
  console.log( Math.floor(Math.random() * Math.pow(10,10)) );
}
var bike = new VehicleConstructor('bike', 2, 1, 5)
bike.vin();
console.log(bike);
