//P2P connections require Peer.JS
//The rest is mostly Three.JS

// Create a camera with a field of view of 75 degrees, an aspect ratio
// that matches the width and height of the window, and a near and far
// clipping plane of 0.1 and 1000 units, respectively
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

// Set the initial position of the camera relative to the player cube
camera.position.set(0, 2, -5);

// Create a renderer
const renderer = new THREE.WebGLRenderer();

// Set the size of the renderer to match the window size
renderer.setSize(window.innerWidth, window.innerHeight);

// Add the renderer's DOM element to the document body
document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();

function addGround(color) {
let c = color || 0x00ff00
// Create an infinite plane and add it to the scene
const planeGeometry = new THREE.PlaneGeometry(100, 100, 100, 100);
const planeMaterial = new THREE.MeshBasicMaterial({color: c});
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = -Math.PI / 2;
scene.add(plane);
return plane
}

function createPlayer() {
// Create a cube geometry
const cubeGeometry = new THREE.BoxGeometry(1, 1, 1);

// Create a material for the cube
const cubeMaterial = new THREE.MeshPhongMaterial({
  color: Math.random() * 0xffffff
});

// Create a mesh with the geometry and material
const playerCube = new THREE.Mesh(cubeGeometry, cubeMaterial);

// Set the initial position of the player cube
playerCube.position.set(0, 5, 0);

// Add the player cube to the scene
scene.add(playerCube);

// Add the camera to the player cube
playerCube.add(camera);
return [playerCube, camera]
}

function p2pChat() {
peer = new Peer("playerid" + math.random);
// Create a textarea for the chat messages
const chatTextarea = document.createElement('textarea');
chatTextarea.rows = 10;
chatTextarea.style.position = 'absolute';
chatTextarea.style.left = '10px';
chatTextarea.style.top = '10px';
document.body.appendChild(chatTextarea);

// Create a button to send chat messages
const chatSendButton = document.createElement('button');
chatSendButton.textContent = 'Send';
chatSendButton.style.position = 'absolute';
chatSendButton.style.left = '10px';
chatSendButton.style.bottom = '10px';
document.body.appendChild(chatSendButton);


function setCollisionsEnabled(object, enabled) {
  object.collidable = !!enabled; // convert to boolean
  return object.collidable
}

function checkCollisions(object) {
return object.collidable
}

function log(toLog) {
console.log(toLog)
}

function logWarn(warning) {
console.warning(warn)
}

function logError(err) {
console.error(err)
}

// When the chat send button is clicked
chatSendButton.addEventListener('click', () => {
  const message = chatTextarea.value.trim();

  if (message) {
    // Send the chat message to the other player
    conn.send({
      type: 'chat',
      message: message
    });

    // Add the chat message to the textarea
    chatTextarea.value += `You: ${message}\n`;
    chatTextarea.scrollTop = chatTextarea.scrollHeight;
  }

  // Clear the chat message input
  chatTextarea.value = '';
});

}

// When a connection to another player is established
peer.on('connection', (conn) => {
  console.log('Connection established with another player!');

  // Listen for updates to the other player's position
  conn.on('data', (data) => {
    console.log('Received data:', data);

    if (data.type === 'position') {
      playerCube.position.set(data.x, data.y, data.z);
    } else if (data.type === 'chat') {
      // Add the chat message to the textarea
      chatTextarea.value += `Other player: ${data.message}\n`;
      chatTextarea.scrollTop = chatTextarea.scrollHeight;
    }
  });
});


function enableP2P() {

//document.body.innerHTML = document.body.innerHTML + "<div id="peer-connection-container"></div>"

// Create a container for the text input, button, and ID label
const peerConnectionContainer = document.createElement('div');
peerConnectionContainer.id = 'peer-connection-container';
document.body.appendChild(peerConnectionContainer);

// Create a text input for entering a peer ID
const peerIdInput = document.createElement('input');
peerIdInput.type = 'text';
peerIdInput.id = 'peer-id-input';
peerConnectionContainer.appendChild(peerIdInput);

// Create a label for the text input
const peerIdLabel = document.createElement('label');
peerIdLabel.textContent = 'Connect to Peer ID:';
peerIdLabel.htmlFor = 'peer-id-input';
peerConnectionContainer.appendChild(peerIdLabel);

// Create a button for connecting to the specified peer ID
const connectButton = document.createElement('button');
connectButton.id = 'connect-button';
connectButton.textContent = 'Connect';
peerConnectionContainer.appendChild(connectButton);

// Create a label for displaying the player's own peer ID
const ownPeerIdLabel = document.createElement('label');
ownPeerIdLabel.textContent = 'Your Peer ID:';
peerConnectionContainer.appendChild(ownPeerIdLabel);

const ownPeerId = document.createElement('span');
ownPeerId.id = 'own-peer-id';
peerConnectionContainer.appendChild(ownPeerId);


// Display the player's own peer ID
ownPeerIdLabel.textContent = peer.id;

// Add a click event listener to the connect button
connectButton.addEventListener('click', () => {
  // Get the peer ID from the text input
  const peerId = peerIdInput.value;

  // Connect to the specified peer ID
  const conn = peer.connect(peerId);

  // Log any errors that occur during the connection process
  conn.on('error', (err) => {
    console.error(err);
  });
});

// When the peer ID is assigned
peer.on('open', (id) => {
  console.log('My peer ID is:', id);

  // Connect to another player with ID 'player2' (testing)
  //const conn = peer.connect('player2');

  // When the connection is opened
  conn.on('open', () => {
    console.log('Connection opened with another player!');

    // Listen for updates to the player's position
        playerCube.position.onChange(() => {
      console.log('Sending position update:', playerCube.position);
      conn.send({
        x: playerCube.position.x,
        y: playerCube.position.y,
        z: playerCube.position.z
      });
    });
  });
});

}


function startPlayerMovement() {
// Define a map of keys and their associated movement directions
const keyMap = {
  'w': 'forward',
  'a': 'left',
  's': 'backward',
  'd': 'right'
};

// Listen for keydown events
document.addEventListener('keydown', (event) => {
  const direction = keyMap[event.key];

  if (direction) {
    // Calculate the movement vector based on the direction and speed
    const movementVector = new THREE.Vector3();

    if (direction === 'forward') {
      movementVector.z = -movementSpeed;
    } else if (direction === 'backward') {
      movementVector.z = movementSpeed;
    } else if (direction === 'left') {
      movementVector.x = -movementSpeed;
    } else if (direction === 'right') {
      movementVector.x = movementSpeed;
    }

    // Apply the movement vector to the player's position
    player.position.add(movementVector);
  }
});
}

// Function to load JavaScript from a URL
function loadScript(url) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = url;
    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
  });
}


function hashString(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = (hash * 31 + str.charCodeAt(i)) & 0xffffffff;
  }
  return hash;
}

function seedrand(seed) {
  let rngState = hashString(seed);
  return function() {
    rngState = (rngState * 1103515245 + 12345) & 0x7fffffff;
    return rngState % 9900000;
  }
}


function generateTerrain(seed) {
  // Define the size of each voxel in world units
  const voxelSize = 1;

  // Create the random number generator based on the seed string
  const random = new seedrand(seed)();

  // Create an empty group to hold the voxels
  const voxelGroup = new THREE.Group();

  // Define a function to generate a single chunk of terrain
  function generateChunk(position) {
    const chunkSize = new THREE.Vector3(16, 16, 16);
    const chunkOrigin = new THREE.Vector3(
      Math.floor(position.x / chunkSize.x) * chunkSize.x,
      Math.floor(position.y / chunkSize.y) * chunkSize.y,
      Math.floor(position.z / chunkSize.z) * chunkSize.z
    );

    for (let x = 0; x < chunkSize.x; x++) {
      for (let z = 0; z < chunkSize.z; z++) {
        // Compute the height of the terrain at this location
        const noiseValue = noise.perlin3(
          (chunkOrigin.x + x) / 50,
          (chunkOrigin.z + z) / 50,
          random.get()
        );

        const height = Math.floor(
          (noiseValue + 1) * chunkSize.y * 0.5 + chunkOrigin.y
        );

        // Generate the voxels for this column of the terrain
        for (let y = 0; y < height; y++) {
          const voxelGeometry = new THREE.BoxGeometry(voxelSize, voxelSize, voxelSize);
          const voxelMaterial = new THREE.MeshLambertMaterial({ color: 0x00ff00 });
          const voxelMesh = new THREE.Mesh(voxelGeometry, voxelMaterial);
          voxelMesh.position.set(
            chunkOrigin.x + x * voxelSize,
            y * voxelSize,
            chunkOrigin.z + z * voxelSize
          );
          voxelMesh.castShadow = true;
          voxelMesh.receiveShadow = true;
          voxelGroup.add(voxelMesh);
        }
      }
    }
  }
}
  // Define a function to update the terrain based on the camera position
  function updateTerrain(cameraPosition) {
    const chunkSize = new THREE.Vector3(16, 16, 16);
    const chunkOrigin = new THREE.Vector3(
      Math.floor(cameraPosition.x / chunkSize.x) * chunkSize.x,
      Math.floor(cameraPosition.y / chunkSize.y) * chunkSize.y,
      Math.floor(cameraPosition.z / chunkSize.z) * chunkSize.z
    );

    // Remove any chunks that are too far away
    voxelGroup.children.forEach((child) => {
      if (
        Math.abs(child.position.x - chunkOrigin.x) > chunkSize.x * 2 ||
        Math.abs(child.position.y - chunkOrigin.y) > chunkSize.y * 2 ||
        Math.abs(child.position.z - chunkOrigin.z) > chunkSize.z * 2
      ) {
        voxelGroup.remove(child);
      }
    });

   // Generate any missing chunks
for (let x = -chunkSize.x * 2; x <= chunkSize.x * 2; x += chunkSize.x) {
  for (let z = -chunkSize.z * 2; z <= chunkSize.z * 2; z += chunkSize.z) {
    const chunkPosition = chunkOrigin.clone().add(new THREE.Vector3(x, 0, z));

    if (
      !voxelGroup.children.some(
        (child) =>
          child instanceof(THREE.Mesh) &&
          child.position.equals(chunkPosition)
      )
    ) {
      generateChunk(chunkPosition);
    }
  }
}

// Initialize the terrain
updateTerrain(new THREE.Vector3(0, 0, 0));

// Return the voxel group
return voxelGroup;
}

function vector3() {
return THREE.Vector3(x,y,z)
}
function rotation(x,y,z) {
return THREE.Euler(Math.PI / x, y, z);
}

// Function to load JavaScript from a string
function loadScriptFromString(scriptString) {
  const script = document.createElement('script');
  script.text = scriptString;
  document.head.appendChild(script);
}

// Function to add a new object to the scene with size, color, and collision properties
function addObject(size = new THREE.Vector3(1, 1, 1), color = 0xffffff, isCollidable = true) {
  // Create a new cube geometry with the provided size
  const geometry = new THREE.BoxGeometry(size.x, size.y, size.z);

  // Create a new material with the provided color
  const material = new THREE.MeshBasicMaterial({ color: color });

  // Create a new mesh with the geometry and material
  const mesh = new THREE.Mesh(geometry, material);

  // Enable or disable collisions for the mesh
  mesh.isCollidable = isCollidable;

  // Add the mesh to the scene
  scene.add(mesh);
  
  return mesh;
}


function startAnimating() {
// Render the scene with the camera
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

// Define a new property called `isCollidable` on the `THREE.Object3D` prototype
Object.defineProperty(THREE.Object3D.prototype, 'isCollidable', {
  get: function() {
    // Return the value of the `_isCollidable` property
    return this._isCollidable !== undefined ? this._isCollidable : true;
  },
  set: function(value) {
    // Set the `_isCollidable` property to the provided value
    this._isCollidable = value;
  }
});

// Define a function to check collision between two objects
function checkCollision(obj1, obj2) {
  if (obj1.isCollidable && obj2.isCollidable) {
    // Get the bounding boxes of the two objects
    const box1 = new THREE.Box3().setFromObject(obj1);
    const box2 = new THREE.Box3().setFromObject(obj2);

    // Check for intersection between the two bounding boxes
    if (box1.intersectsBox(box2)) {
      // Stop the object that is colliding
      obj1.position.copy(obj1.lastPosition);
      obj2.position.copy(obj2.lastPosition);
      return true;
    }
  }

  return false;
}

// Define a function to update the position of a collidable object
function updateCollidableObjectPosition(object, delta) {
  // Save the last position of the object
  object.lastPosition = object.position.clone();

  // Update the position of the object
  object.position.addScaledVector(object.velocity, delta);
}

// Use the `checkCollision()` function to handle collisions in the animation loop
function animate() {
  // Calculate the time elapsed since the last frame
  const delta = clock.getDelta();

  // Update the position of each collidable object
  collidableObjects.forEach(object => {
    updateCollidableObjectPosition(object, delta);
  });

  // Check for collisions between each pair of collidable objects
  for (let i = 0; i < collidableObjects.length; i++) {
    for (let j = i + 1; j < collidableObjects.length; j++) {
      checkCollision(collidableObjects[i], collidableObjects[j]);
    }
  }

  // Render the scene
  renderer.render(scene, camera);

  // Request the next frame
  requestAnimationFrame(animate);
}

animate();
}
