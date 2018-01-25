import math
def generateSVG(mapdata):
  # If fog, just gray image
  if 'weather' in mapdata:
    if 'type' in mapdata['weather']:
      if mapdata['weather']['type'] == 'fog':
        return fog()

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

  routeColorByType = {
    'default': '#a67f4c',
    'dying_road': '#5fa17c',
    'weight_limit': '#402a16'
  }

  # Routes to dict (index for node ID)
  routeI = {}
  for i, route in enumerate(mapdata['routes']):
    routeI[route['route_node']] = i

  # Draw routes
  for route in mapdata['routes']:    
    if len(route['to']) > 0:
      for dest in route['to']:
        destI = routeI[mapdata['routes'][routeI[dest]]['route_node']]
        svg += drawRoute(
          route['x'] + xOff,
          route['y'] + yOff,
          mapdata['routes'][destI]['x'] + xOff,
          mapdata['routes'][destI]['y'] + yOff,
          routeColorByType['default']
        )

  # Draw anomalies
  for route in mapdata['routes']:
    routeColor = routeColorByType['default']

    if 'anomalies' in route and len(route['anomalies']) > 0:
      for anomaly in route['anomalies']:
        if 'dying_road' in anomaly:
          routeColor = routeColorByType['dying_road']
        if 'weight_limit' in anomaly:
          routeColor = routeColorByType['weight_limit']

        if 'one_way_road' in anomaly and 'to' in anomaly:
          destI = routeI[mapdata['routes'][routeI[anomaly['to']]]['route_node']]
          x1 = route['x'] + xOff
          x2 = mapdata['routes'][destI]['x'] + xOff
          y1 = route['y'] + yOff
          y2 = mapdata['routes'][destI]['y'] + yOff   
          svg += drawArrow((x1 + x2) / 2, (y1 + y2) / 2, angleBetween(x1, x2, y1, y2) + 135)
        elif 'to' in anomaly:
          destI = routeI[mapdata['routes'][routeI[anomaly['to']]]['route_node']]
          svg += drawRoute(
            route['x'] + xOff,
            route['y'] + yOff,
            mapdata['routes'][destI]['x'] + xOff,
            mapdata['routes'][destI]['y'] + yOff,
            routeColor
          )

  #Draw nodes
  for route in mapdata['routes']:
    svg += ('<circle cx="' +
    str(route['x'] + xOff) + '" cy="' +
    str(route['y'] + yOff) + '" r="25" fill="' + routeColorByType['default'] + '" />')

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

def drawRoute(x1, y1, x2, y2, color):
  return ('<path d="M' +
    str(x1) + ' ' +
    str(y1) + ' L' +
    str(x2) + ' ' +
    str(y2) + '" stroke="' + color + '" stroke-width="50" />')

def drawArrow(x, y, angle):
  return ('<rect' +
    ' x="' + str(x) +
    '" y="' + str(y) +
    '" width="30"' +
    ' height="30"' +
    ' fill="#402a16"'
    ' transform="rotate(' + str(angle) + ', ' + str(x) + ', ' + str(y) + ')" />' + '<rect' +
    ' x="' + str(x+5) +
    '" y="' + str(y+5) +
    '" width="30"' +
    ' height="30"' +
    ' fill="#a67f4c"'
    ' transform="rotate(' + str(angle) + ', ' + str(x) + ', ' + str(y) + ')" />')

def angleBetween(x1, x2, y1, y2):
  return math.degrees(math.atan2(y2 - y1, x2 - x1))

def fog():
  return '<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink= "http://www.w3.org/1999/xlink"><rect width="100" height="100" x="0" y="0" fill="#7F7F7F" /></svg>'

def findNodeIndex(routes, nodeID):
  pass
