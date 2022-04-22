import ProjectileController from './ProjectileController'

export default class BeamController extends ProjectileController {
  constructor(options) {
    options.items = ['charge-beam', 'ice-beam', 'wave-beam', 'spazer-beam', 'plasma-beam']
    super(options)
  }
}
