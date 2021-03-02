# Explanations

Write a script that given the name of a tv series outputs all episodes, sorted by average ratings.

For example,

```bash
$ python solution.py 'Breaking Bad'
S05E14 Ozymandias                               10.0
S04E13 Face Off                                 9.9
S05E16 Felina                                   9.9
S05E13 To'hajiilee                              9.8
S03E13 Full Measure                             9.7
S04E11 Crawl Space                              9.7
S05E15 Granite State                            9.7
S05E05 Dead Freight                             9.7
S03E07 One Minute                               9.6
S04E10 Salud                                    9.6
S05E11 Confessions                              9.6
S05E07 Say My Name                              9.6
S05E08 Gliding Over All                         9.6
S03E12 Half Measures                            9.5
S04E12 End Times                                9.5
S05E09 Blood Money                              9.5
S01E06 Crazy Handful of Nothin'                 9.3
S02E12 Phoenix                                  9.3
S02E13 ABQ                                      9.3
S02E02 Grilled                                  9.3
S03E06 Sunset                                   9.3
S04E08 Hermanos                                 9.3
S05E01 Live Free or Die                         9.3
S02E08 Better Call Saul                         9.2
S02E09 4 Days Out                               9.2
S04E01 Box Cutter                               9.2
S05E10 Buried                                   9.2
S05E12 Rabid Dog                                9.2
S01E01 Pilot                                    9.1
S05E06 Buyout                                   9.1
S01E07 A No-Rough-Stuff-Type Deal               8.9
S02E11 Mandala                                  8.9
S02E06 Peekaboo                                 8.9
S04E07 Problem Dog                              8.9
S04E09 Bug                                      8.9
S05E02 Madrigal                                 8.9
S05E03 Hazard Pay                               8.9
S05E04 Fifty-One                                8.9
S01E03 ...And the Bag's in the River            8.8
S03E08 I See You                                8.8
S01E02 Cat's in the Bag...                      8.7
S02E01 Seven Thirty-Seven                       8.7
S02E07 Negro y Azul                             8.7
S03E02 Caballo sin Nombre                       8.7
S03E05 Más                                      8.7
S04E04 Bullet Points                            8.7
S04E05 Shotgun                                  8.7
S02E10 Over                                     8.6
S03E01 No Más                                   8.6
S03E03 I.F.T.                                   8.5
S03E11 Abiquiu                                  8.5
S03E09 Kafkaesque                               8.5
S04E06 Cornered                                 8.5
S01E05 Gray Matter                              8.4
S02E03 Bit by a Dead Bee                        8.4
S02E05 Breakage                                 8.4
S01E04 Cancer Man                               8.3
S02E04 Down                                     8.3
S03E04 Green Light                              8.3
S04E02 Thirty-Eight Snub                        8.3
S04E03 Open House                               8.1
S03E10 Fly                                      7.8

$ python solution.py "Game of Thrones"
S03E09 The Rains of Castamere                   9.9
S05E08 Hardhome                                 9.9
S06E09 Battle of the Bastards                   9.9
S06E10 The Winds of Winter                      9.9
S07E04 The Spoils of War                        9.8
S02E09 Blackwater                               9.7
S04E02 The Lion and the Rose                    9.7
S04E08 The Mountain and the Viper               9.7
S04E10 The Children                             9.7
S04E06 The Laws of Gods and Men                 9.7
S06E05 The Door                                 9.7
S01E09 Baelor                                   9.6
S03E04 And Now His Watch Is Ended               9.6
S04E09 The Watchers on the Wall                 9.6
S01E10 Fire and Blood                           9.5
S05E09 The Dance of Dragons                     9.5
S02E10 Valar Morghulis                          9.4
S06E02 Home                                     9.4
S07E07 The Dragon and the Wolf                  9.4
S01E06 A Golden Crown                           9.2
S01E07 You Win or You Die                       9.2
S03E10 Mhysa                                    9.2
S07E03 The Queen's Justice                      9.2
S01E01 Winter Is Coming                         9.1
S01E05 The Wolf and the Lion                    9.1
S02E06 The Old Gods and the New                 9.1
S04E01 Two Swords                               9.1
S04E07 Mockingbird                              9.1
S05E10 Mother's Mercy                           9.1
S06E04 Book of the Stranger                     9.1
S01E08 The Pointy End                           9.0
S03E05 Kissed by Fire                           9.0
S03E08 Second Sons                              9.0
S05E07 The Gift                                 9.0
S07E06 Beyond the Wall                          9.0
S02E07 A Man Without Honor                      8.9
S03E03 Walk of Punishment                       8.9
S04E03 Breaker of Chains                        8.9
S07E02 Stormborn                                8.9
S01E02 The Kingsroad                            8.8
S01E04 Cripples, Bastards, and Broken Things    8.8
S02E01 The North Remembers                      8.8
S02E04 Garden of Bones                          8.8
S02E03 What Is Dead May Never Die               8.8
S02E05 The Ghost of Harrenhal                   8.8
S02E08 The Prince of Winterfell                 8.8
S03E01 Valar Dohaeris                           8.8
S03E06 The Climb                                8.8
S04E04 Oathkeeper                               8.8
S04E05 First of His Name                        8.8
S07E05 Eastwatch                                8.8
S01E03 Lord Snow                                8.7
S03E07 The Bear and the Maiden Fair             8.7
S05E04 Sons of the Harpy                        8.7
S06E03 Oathbreaker                              8.7
S03E02 Dark Wings, Dark Words                   8.6
S05E05 Kill the Boy                             8.6
S06E07 The Broken Man                           8.6
S07E01 Dragonstone                              8.6
S02E02 The Night Lands                          8.5
S05E01 The Wars to Come                         8.5
S06E01 The Red Woman                            8.5
S05E02 The House of Black and White             8.5
S05E03 High Sparrow                             8.5
S06E06 Blood of My Blood                        8.4
S06E08 No One                                   8.4
S05E06 Unbowed, Unbent, Unbroken                8.0
S08E02 A Knight of the Seven Kingdoms           7.8
S08E01 Winterfell                               7.5
S08E03 The Long Night                           7.4
S08E05 The Bells                                5.9
S08E04 The Last of the Starks                   5.4
S08E06 The Iron Throne                          4.0
```
