import ToolStorage from '@/components/unrest/ToolStorage'
import { LAYER_NAMES, INITIAL_LAYERS } from './ConfigPopper.vue'

export default (component) => {
  const getTools = () => {
    const tools = [
      {
        slug: 'settings_open',
        icon: 'fa fa-cogs',
        select: ToolStorage.TOGGLE,
      },
      {
        slug: 'run_path',
        icon: 'fa fa-run',
      },
    ]
    if (component.$auth.user?.is_superuser) {
      return [
        ...tools,
        { slug: 'select', icon: 'fa fa-mouse-pointer' },
        { slug: 'move_zone', icon: 'fa fa-object-group' },
        { slug: 'move_room', icon: 'fa fa-th' },
        { slug: 'edit_room', icon: 'fa fa-edit' },
        {
          slug: 'elevator',
          icon: (_t, v) => `sm-elevator -${v}`,
          variants: ['brinstar', 'tourian', 'maridia', 'norfair', 'line'],
        },
        {
          slug: 'video_path',
          icon: 'fa fa-youtube-play',
        },
      ]
    }
    return tools
  }

  const initial = INITIAL_LAYERS
  const storage = ToolStorage('tools__dread', { tools: getTools, initial })
  storage.getVisibleLayers = () => LAYER_NAMES.filter((n) => storage.state[`show_${n}`])
  storage.all_layers = LAYER_NAMES

  return storage
}
