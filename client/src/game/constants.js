export const SCENERY_GROUP = Math.pow(2, 1)
export const BULLET_GROUP = Math.pow(2, 2)
export const PLAYER_GROUP = Math.pow(2, 3)
export const ITEM_GROUP = Math.pow(2, 4)

export const DIRECTIONS = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
]

export const DXYS = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
]

export const PLAYER_ACTIONS = [
  'up',
  'down',
  'left',
  'right',
  'shoot1',
  'shoot2',
  'special',
  'swap',
  'jump',
  'run',
  'aimup',
  'aimdown',
  'pause',
]

export const POSTURE = {
  ball: 0,
  crouch: 1,
  stand: 2,
  spin: 3,
  _heights: [14 / 16, 30 / 16, 42 / 16, 24 / 16],
}

export const CHARGE_TIME = 1000

export const ENERGY = {
  total_tanks: 14,
  total_reserve: 4,
  base_energy: 99,
  per_pack: {
    missile: 5,
    'super-missile': 5,
    'power-bomb': 5,
    'reserve-tank': 100,
    'energy-tank': 100,
  },
}
