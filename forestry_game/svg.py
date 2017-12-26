import math
def generateSVG(mapdata):
  svg = ''

  # Find smallest and largest x and y values and set offsets and dimensions
  xMin, yMin, xMax, yMax = float('inf'), float('inf'), -float('inf'), -float('inf')
  # Give the result image some padding
  padding = 100

  for route in mapdata['routes']:
    if route['x'] < xMin:
      xMin = route['x']
    if route['y'] < yMin:
      yMin = route['y']
    if route['x'] > xMax:
      xMax = route['x']
    if route['y'] > yMax:
      yMax = route['y']

  for log in mapdata['logs']:
    if log['x'] < xMin:
      xMin = log['x']
    if log['y'] < yMin:
      yMin = log['y']
    if log['x'] > xMax:
      xMax = log['x']
    if log['y'] > yMax:
      yMax = log['y']

  for logdeposit in mapdata['logdeposits']:
    if logdeposit['x'] < xMin:
      xMin = logdeposit['x']
    if logdeposit['y'] < yMin:
      yMin = logdeposit['y']
    if logdeposit['x'] > xMax:
      xMax = logdeposit['x']
    if logdeposit['y'] > yMax:
      yMax = logdeposit['y']

  xOff = 0 - xMin + padding
  yOff = 0 - yMin + padding
  width = xMax + xOff + padding
  height = yMax + yOff + padding

  # Draw routes
  for route in mapdata['routes']:
    if len(route['to']) > 0:
      for dest in route['to']:
        for routeTo in mapdata['routes']:
          if routeTo['route_node'] == dest:
            svg += ('<path d="M' +
            str(route['x'] + xOff) + ' ' +
            str(route['y'] + yOff) + ' L' +
            str(routeTo['x'] + xOff) + ' ' +
            str(routeTo['y'] + yOff) + '" stroke="#a67f4c" stroke-width="50" />')
    svg += ('<circle cx="' +
    str(route['x'] + xOff) + '" cy="' +
    str(route['y'] + yOff) + '" r="25" fill="#a67f4c" />')

  logColorByType = [
    '#a28569',
    '#e4d73d',
    '#f27f1a',
    '#d85040',
    '#946fed',
    '#2c57c3'
  ]

  # Draw logs
  for log in mapdata['logs']:
    logColor = logColorByType[log['type']]
    if not 'rot' in log:
      log['rot'] = 0

    svg += ('<path d="M' +
    str(log['x'] + xOff - 25) + ' ' +
    str(log['y'] + yOff) +' L' +
    str(log['x'] + xOff + 25) + ' ' +
    str(log['y'] + yOff) + '" stroke="' + logColor + '" stroke-width="5" ' + 
    'transform="rotate(' + str(math.degrees(log['rot']))  + ' ' + str(log['x'] + xOff) + ' ' + str(log['y'] + yOff) + ')" />')

  # Draw log deposits
  for logdeposit in mapdata['logdeposits']:
    depositColor = '#333333'
    if 'type' in logdeposit:
      depositColor = logColorByType[logdeposit['type']]
    if not 'rot' in logdeposit:
      logdeposit['rot'] = 0
    svg += ('<rect width="150" height="50" style="fill:' + depositColor + '" x="' +
    str(logdeposit['x'] + xOff - 75) + '" y="' +
    str(logdeposit['y'] + yOff - 25) + '" '+
    'transform="rotate(' + str(math.degrees(logdeposit['rot']))  + ' ' + str(logdeposit['x'] + xOff) + ' ' + str(logdeposit['y'] + yOff) + ')" />')

  # Draw startpoint
  svg += ('<circle r="15" fill="#FFDE00" stroke="#000000" stroke-width="2" cx="' +
  str(mapdata['startpoint']['x'] + xOff) + '" cy="' +
  str(mapdata['startpoint']['y'] + yOff) + '" />')

  return ('<svg width="' + str(width) +
  '" height="' + str(height) +
  '" xmlns="http://www.w3.org/2000/svg" xmlns:xlink= "http://www.w3.org/1999/xlink">' + 
  svg + '</svg>')
  