// Create a VehicleConstructor that takes in the name, number of wheels, and number of passengers. Then complete the following tasks:
  // Each vehicle should have a makeNoise method
  // Using the constructor, create a Bike
  // Redefine the Bike’s makeNoise method to print “ring ring!”
  // Create a Sedan
  // Redefine the Sedan’s makeNoise method to print “Honk Honk!”
  // Using the constructor, create a Bus
  // Add a method to Bus that takes in the number of passengers to pick up and adds them to the passenger count​

function VehicleConstructor(name, noise) {
  this.name =  name,
  this.noise = noise,
  this.makeNoise = function(noise) {
    console.log(noise);
  }
}

var bike  = new VehicleConstructor('Bike', "ring, ring!")
console.log(bike.name);
console.log(bike.noise);

var sedan = new VehicleConstructor('Sedan', 'Honk Honk!')
console.log(sedan.name);
console.log(sedan.noise);

var bus = new VehicleConstructor('Bus')
bus.passengers = 0
bus.toPickUp = function(number) {
  bus.passengers += number;
}
console.log(bus);
console.log(bus.name)
console.log(bus.passengers);
bus.toPickUp(10);
console.log(bus.passengers)
