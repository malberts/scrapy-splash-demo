function main(splash, args)
  splash.images_enabled = false
  splash:go(args.url)
  splash:wait(5)

  -- A function to count the number of items on the page.
  local count_items = splash:jsfunc([[
    function() {
      return document.getElementsByClassName('searchItem').length;
    }
  ]])

  -- A target of -1 means everything.
  local target_count = -1

  -- Use the specified target count.
  -- The script will stop once the target amount is reached.
  if args.target_count and args.target_count > 0 then
    target_count = args.target_count
  end
  print('Target count: ' .. target_count)

  local has_enough = false
  local end_of_page = false
  local last_count = 0

  -- Keep scrolling down until enough items are found, or the end of the page
  -- is reached.
  local scroll_counter = 1
  repeat
    print('Scroll iteration: ' .. scroll_counter)
    last_count = count_items()

    local last_y = splash.scroll_position['y']
    splash:runjs('window.scrollTo(0, document.body.scrollHeight)')

    -- Wait for 10 new items (as per the website) to appear within 5 seconds.
    -- Check every 0.5 seconds.
    local new_count
    for i=1,10 do
      splash:wait(0.5)
      new_count = count_items()
      if new_count >= last_count + 10 then break end
    end

    print("New count: " .. new_count)

    -- If we found enough items.
    has_enough = target_count > 0 and new_count >= target_count

    -- If the end of the page is reached, stop.
    end_of_page = splash.scroll_position['y'] == last_y

    scroll_counter = scroll_counter + 1
  until (has_enough or end_of_page)

  return {
    png = splash:png(),
    html = splash:html(),
    count = count_items(),
  }
end
